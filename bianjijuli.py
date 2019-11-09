'''
最短编辑距离
'''

def  LevenshteinDis(str1, str2):
    dp = [[i+j for j in range(len(str2)+1)] for i in range(len(str1)+1)]
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                d = 0
            else:
                d =1
            dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+d)
    return dp[len(str1)][len(str2)]


if __name__ == '__main__':
    print(LevenshteinDis('aba', 'aab'))
