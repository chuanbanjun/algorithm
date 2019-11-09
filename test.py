def solution(nums):
    res = []
    def dfs(num, path):
        if not num:
            res.append(path)
            return
        for i in range(len(num)):
            dfs(num[:i]+num[i+1:], path+[num[i]])
    dfs(nums, [])
    return res 
            
if __name__ == '__main__':
    n = int(input())
    nums = input().split()

    res = solution(nums)
    for i in res:
        print(' '.join(i))
     