'''
一串首尾相边的珠子（m个），有N种颜色，设计 一种算法，取出其中一段，要求包含所有N种颜色，并使长度最短。
给一个字符串s1,和一个小串s2，求算法能在s1中找到包含s2里所有字符的最小子串。比如：
s1 = “ADOBECODEBANC”
s2 = “ABC”
最小子串是 “BANC”，要求O(N)的算法。
'''
'''
用两个变量 front rear 指向一个的子串区间的头和尾
用一个int cnt[255]={0}记录当前这个子串里 字符集a,b,c 各自的个数，一个变量sum记录字符集里有多少个了
rear 一直加，更新cnt[]和sum的值，直到 sum等于字符集个数
然后front++,直到cnt[]里某个字符个数为0，这样就找到一个符合条件的字串了
'''
import sys

def findsubstring(str1,str2):
    dict = {}
    for i in range(0x41, 0x5A):
        dict[chr(i)] = -1
    for i in str2:
        dict[i] = 0

    p1,p2,min_p1,min_p2,count = 0,0,0,0,0
    len_str2 = len(str2)
    minlen = sys.maxsize

    while p2!=len(str1) or len_str2==count:
        if count<len_str2:
            if dict[str1[p2]]==0:
                count += 1
                dict[str1[p2]] += 1
            elif dict[str1[p2]]>0:
                dict[str1[p2]] += 1
            p2 += 1

        if count==len_str2:
            if p2-p1<minlen:
                min_p1=p1
                min_p2=p2
                minlen=min_p2-min_p1
            dict[str1[p1]] -= 1
            if dict[str1[p1]]==0:
                count -= 1
            p1 += 1

    if min_p1 <= min_p2:
            print(str1[min_p1:min_p2])
    return minlen

if __name__ == '__main__':
    s1 = 'ADOBECODEBANC'
    s2 = 'ABC'
    print(findsubstring(s1,s2))