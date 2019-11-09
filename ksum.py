'''
输入两个整数n和sum，从数列1,2,3...n中抽取和为sum的所有组合
'''
'''
dp(i,j)表示S中前i个元素的子集和等于j的情况，则
若S[i] > j，则S[i]不在子集s中。
若S[i] <= j, 则有以下两种情况：
    一种情况是S[i]不在子集s中，dp(i, j) = dp(i-1, j); 
    一种情况是S[i]在子集s中，dp(i, j)= dp(i-1, j-S[i]).
'''


def isSubsetSum(lis, n):
    len_lis = len(lis)
    dp = [[True] * (n + 1) for _ in range(len_lis + 1)]

    # n为0，True
    for i in range(0, len_lis+1):
        dp[i][0] = True

    # lis为空，False
    for i in range(1, n + 1):
        dp[0][i] = False

    for i in range(1, len_lis+1):
        for j in range(1, n + 1):
            if j < lis[i - 1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - lis[i - 1]]

    if dp[len_lis][n]:
        result = []
        i = len_lis
        while i >= 0:
            if dp[i][n] and not dp[i - 1][n]:
                result.append(lis[i - 1])
                n -= lis[i - 1]
            if n == 0:
                break
            i -= 1
        return result
    else:
        return False


if __name__ == '__main__':

    lis = [1, 3, 4, 9]
    n = 7
    print(isSubsetSum(lis, n))