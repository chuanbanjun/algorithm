'''
一个数字串'2??3??'，‘?'位置可以填入0~9，
问最后组成的数mod13余数为5的填数个数
'''
'''
记dp[i][k]表示前i位组成的数mod 13余数为k的情况数,k=0,1,...,12，
那么dp[i+1][(j*pow(10,i+1)+k)%13] += dp[i][k], j表示可以选择的数字
(如果是?那就是0~9均可，如果固定那就只有1种选择)
'''

s = input()[::-1]
_MO = pow(10,9)+7
result = [0 for _ in range(13)]
for i in range(len(s)):
    if i == 0:
        if s[i] == '?':
            for j in range(10):
                result[j] = 1
        else:
            result[int(s[i])] = 1
    else:
        temp = [0 for _ in range(13)]
        bias = pow(10,i)%13
        if s[i] == '?':
            for j in range(10):
                for k in range(13):
                    temp[(k+j*bias)%13] += result[k]
        else:
            j = int(s[i])
            for k in range(13):
                temp[(k+j*bias)%13] += result[k]
        result = [temp[i]%_MO for i in range(13)]
print(result[5]%_MO)
