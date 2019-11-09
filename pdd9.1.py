'''
小梅和他男朋友小白玩游戏，
小梅有N <= 8张牌， 小白有 M <= N张牌, 小梅将牌从左往右铺开（不一定排序）
 ，小白同样将自己的牌从左往右铺开
小梅对自己的牌从左到右进行N个回合的操作，生成一个新的牌序列， 每个回合操作有如下三种选择
1. d   取出一张牌 丢掉
2. l   取出一张牌 将他放在 新序列的左边
3. r   取出一张牌 将他放在 新序列的右边
当 新序列 = 小白的牌序列时，  小梅赢，  求 小梅能够获胜的所有的赢法
'''

s = int(input())
def cmp(s1,s2):
    if len(s1)!=len(s2):
        return False
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            return False
    return True
for i in range(s):
    nums = [char for char in input()]
    news = [char for char in input()]
    n = len(nums)
    paths = []
    def search(nums,luans,news,path,n):
        if n == 0:
            if cmp(luans,news):
                paths.append(path)
            return
        num = nums[0]
        nums = nums[1:]
        search(nums,luans,news,path+['d'],n-1)
        search(nums,[num]+luans,news,path+['l'],n-1)
        search(nums,luans+[num],news,path+['r'],n-1)
    search(nums,[],news,[],n)
    print ('{')
    for path in paths:
        print (' '.join(path))
    print ('} ')
