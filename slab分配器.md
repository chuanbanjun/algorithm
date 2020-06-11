## 概述

伙伴系统是以page为单位进行操作的。但是很多内存需求是以Byte为单位的,并不需要如此大的内存分配，slab就是用在这种场景的

slab分配器最终还是由伙伴系统来分配出实际的物理页面，只不过slab分配器在这些连续的物理页面上实现了自己的算法，以此来对小内存块进行管理

slab分配器提供以下接口:

```c
//创建slab描述符kmem_cache，此时并没有真正分配内存
struct kmem_cache *kmem_cache_create(const char *, size_t, size_t,unsigned long, void (*)(void *));
//分配slab缓存对象
void *kmem_cache_alloc(struct kmem_cache *, gfp_t flags);
//释放slab缓存对象
void kmem_cache_free(struct kmem_cache *, void *);
//销毁slab描述符
void kmem_cache_destroy(struct kmem_cache *);
```

## 创建slab描述符

slab描述符为struct kmem_cache数据结构(include/linux/slab_def.h)

- cpu_cache：一个Per-CPU的struct kmem_cache数据结构，表示本地CPU缓冲池
- batchcount：表示当前CPU本地缓冲池array_cache为空时，从共享缓冲池或者slabs_partial/slabs_free列表中获取对象的数目
- limit：表示当本地对象缓冲池空闲对象数目大于limit时就会主动释放batchcount个对象，便于内核回收和销毁slab
- shared：用于多核系统
- size：对象长度，要加上align对齐字节
- flags：分配掩码
- num：一个slab可以有多少个对象
- gfporder：此slab占用z^gfporder个页面
- colour：一个slab有几个不同的cache line
- colour_off：一个cache order的长度，和L1 Cache Line长度相同
- freelist_size：每个对象要占1Byte来存放freelist
- name：slab描述符的名称
- object_size：对象的实际大小
- align：对齐的大小
- node：slab对应的节点的struct kmem_cache_node数据结构

slab描述符给每个CPU都提供一个对象缓冲池(struct array_cache)

- avail：对象缓冲池中可用的对象数目
- touched：从缓冲池移除一个对象时，touched置1；收缩缓存时，touched置0
- entry：保存对象的实体

**mm/slab_common.c/kmem_cache_node()**

参数有name：slab描述符的名称，size：缓存对象的大小，align：对齐的大小，flags：分配掩码，ctor：对象的构造函数

1. __kmem_cache_alias()检查是否有现成的slab描述符可用，有即跳转到out_unlock
2. do_kmem_cache_create()调用do_kmem_cache_create创建slab描述符

**kmem_cache_node() -> do_kmem_cache_create()**

将主要参数配置到slab描述符，然后将得到的描述符加入slab_caches全局链表中

**kmem_cache_node() -> do_kmem_cache_create() -> \__kmem_cache_create**

1. 检查size是否和系统的word长度对齐(BYTES_PER_WORD)
2. cachep->align对齐大小设置到struct kmem_cache
3. slab_is_available()判断slab_state>=UP时，可以使用GFP_KERNEL分配，否则只能使用GFP_NOWAIT
4. ALIGN()根据size和align对齐关系计算最终size大小
5. calculate_slab_order()计算相关参数
6. cache_line_size()得出L1 cache行的大小
7. setup_cpu_cache()根据slab_state状态进行不同处理，计算limit/batchcount，分配本地对象缓冲池，共享对象缓冲池

**kmem_cache_node() -> do_kmem_cache_create() -> \__kmem_cache_create -> calculate_slab_order()**

calculate_slab_order()计算一个slab需要分配多少个物理页面，返回值是page order。同时也计算此slab中可以容纳多少个同样大小的对象。

for循环里从0开始计算最合适的gfporder值，最多支持的页面数是2^KMALLOC_MAX_ORDER

KMALLOC_MAX_ORDER由include/linux/slab.h/calculate_slab_order()函数调用cache_eastimate()根据当前大小2^gfporder来计算可以容纳多少个对象，以及剩下多少空间用于cache colour着色

**kmem_cache_node() -> do_kmem_cache_create() -> \__kmem_cache_create -> calculate_slab_order() -> setup_cpu_cache() -> enable_cpucache()**

1. 根据对象大小计算空闲对象的最大阈值limit
2. 在SMP系统中且slab对象大小不大于一个页面的情况下，shared为8
3. 计算batchcount数目，一般用于本地缓冲池和共享缓冲池之间填充对象的数量
4. 调用do_tune_cpucache()配置slab描述符

**kmem_cache_node() -> do_kmem_cache_create() -> \__kmem_cache_create -> calculate_slab_order() -> setup_cpu_cache() -> enable_cpucache() -> do_tune_cpucache()**

1. 通过alloc_kmem_cache_cpus()分配Per-CPU类型的struct array_cache数据结构，即对象缓冲池
2. 调用alloc_kmem_cache_node()来继续初始化slab缓冲区cachep->kmem_cache_node数据结构

## 分配slab对象

kmem_cache_alloc是slab分配缓存对象的核心函数，在slab分配缓存过程中是全程关闭本地中断的

**kmem_cache_alloc-->slab_alloc-->__do_cache_alloc -> \_\_cache_alloc**

1. cpu_cache_get获取本地对象缓冲池ac
2. 本地对象缓冲池是否有空闲对象，ac->avail表示本地对象缓冲池中有空闲对象，可通过ac_get_obj()来分配对象

**kmem_cache_alloc-->slab_alloc-->__do_cache_alloc -> \_\_cache_alloc -> cache_alloc_refill()**

cpu_cache_get获取本地对象缓冲池ac，判断共享对象缓冲池n->shared中有没有空闲的对象。如有，尝试迁移batchcount个空闲对象到本地对象缓冲池ac中(transfer_objects())；如无，查看slab节点中的slabs_partial链表和slabs_free链表，如有空闲对象，则迁移；如都为空，则需重新分配slab(cache_grow())后挂入slabs_free

## 释放slab对象

slab释放对象通过kmem_cache_free进行，在释放过程中也是全程关中断的

一个slab描述符中可能有多个对象，因此释放对象需要两个参数才能确定释放内容

**mm/slab.c/kmem_cache_free()**

1. cache_from_obj()通过要释放对象obj的虚拟地址找到对应的struct kmem_cache数据结构
2. local_irq_save()关闭本地CPU中断
3. __cache_free()将对象释放到本地对象缓冲池ac中

**kmem_cache_free() -> cache_from_obj**

由对象的虚拟地址通过virt_to_pfn()找到对应的pfn，然后通过pfn_to_page()由pfn找到对应的page结构

## kmalloc

kmalloc函数基于slab机制，分配的内存大小也是对齐到2^order个字节，分别命名为kmalloc-16、kmalloc-32、kmalloc-64···的slab描述符，这些kmalloc-xxx的slab描述符是由create_kmalloc_caches在系统初始换的时候创建的(start_kernel -> mm_init -> kmem_cache_init -> create_kmalloc_caches)

**kmalloc() -> kmalloc_index()**

查找使用的是哪个slab缓冲区