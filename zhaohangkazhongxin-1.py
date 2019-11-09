'''
给定一个移动字符串'RLRLLR'表示机器人在位置i时的移动方向，
R向右L向左，每个时刻移动一次，问开始时每个位置有1个，
移动pow(10,100)次后每个位置有几个？
'''
'''
最终移动步骤一定会归到L->R->L的循环，所以对于第i个位置，如果是R，
那么向右找到第一个L的位置j就是i号机器人的最终循环地区，
到底是j-1还是j看一下j-i的奇偶即可，如果是奇数说明i向右移动了奇数步，
那么由于pow(10,100)是偶数，所以最终位置为j-1，否则为j；同理如果i号初始为L，
那么向左找到第一个R，同样看奇偶即可
'''

def solution(s):
    final_idx = [None for _ in s]
    result = [0 for _ in s]
    for i in range(len(s)):
        if i == 0:
            j = 0
            while j<len(s) and s[j] == 'R':
                j += 1
            final_idx[i] = j if j%2==0 else j-1
        else:
            if s[i] == s[i-1]:
                if s[i] == 'R':
                    final_idx[i] = final_idx[i-1]-1 if s[final_idx[i-1]] == 'L' else final_idx[i-1]+1
                else:
                    final_idx[i] = final_idx[i-1]+1 if s[final_idx[i-1]] == 'R' else final_idx[i-1]-1
            else:
                if s[i] == 'R':
                    j = i
                    while j<len(s) and s[j] == 'R':
                        j += 1
                    final_idx[i] = j if (j-i)%2==0 else j-1
                else:
                    j = i
                    while j>=0 and s[j]=='L':
                        j -= 1
                    final_idx[i] = j if (i-j)%2==0 else j+1
    for i in range(len(final_idx)):
        result[final_idx[i]] += 1
    return ' '.join(list(map(str,result)))

if __name__ == '__main__':
    s = input()
    print(solution(s))