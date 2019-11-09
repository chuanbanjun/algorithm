'''
全排列
'''
'''
1、递归
'''
def permutation(nums, p, q):
    if p == q:
        s.append(list(nums))
    else:
        for i in range(p, q):
            nums[i], nums[p] = nums[p], nums[i]
            permutation(nums, p+1, q)
            nums[i], nums[p] = nums[p], nums[i]

if __name__ == '__main__':
    s= []
    nums = [i for i in range(1, 4)]
    permutation(nums, 0, len(nums))
    print(s)


'''
2、dfs
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(num, path):
            if not num:
                res.append(path)
                return
            for i in range(len(num)):
                dfs(num[:i]+num[i+1:], path+[num[i]])
        dfs(nums, [])
        return res 