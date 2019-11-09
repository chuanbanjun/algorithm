'''
在一根无限长的数轴上，你站在0的位置。终点在target的位置。
每次你可以选择向左或向右移动。第 n 次移动（从 1 开始），可以走 n 步。
返回到达终点需要的最小移动次数。
'''
'''
当超过目标值的差值d为偶数时，只要将第 d/2 步的距离取反，
就能得到目标值，此时的步数即为到达目标值的步数。
那么，如果d为奇数时，且当前为第n步，那么我们看下一步 n+1 的奇偶，
如果 n+1 为奇数，那么加上 n+1 再做差，得到的差值就为偶数了，
问题解决，如果 n+1 为偶数，那么还得加上 n+2 这个奇数，
才能让差值为偶数，这样就多加了两步。
'''

def solution(target):
    target = abs(target)
    n,n_sum = 0,0
    while n_sum<target or (n_sum-target)%2==1:
        n+=1
        n_sum+=n
    return n

if __name__ == '__main__':
    target = int(input())
    print(solution(target))
