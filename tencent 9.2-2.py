# ????????????????
import sys

line = sys.stdin.readline().strip().split()
n, k = int(line[0]), int(line[1])
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))


def iscontinuity(lis, k, l):
    if len(lis) == 0 or len(lis) != l:
        return False
    index_lis = [i for i, x in enumerate(lis) if x == 'w']
    if len(index_lis) % k != 0:
        return False
    w_str = ''.join(['w'] * k)
    all_str = ''.join(lis)
    if all_str.count(w_str) * k == len(index_lis):
        return True
    else:
        return False


for m in matrix:
    a, b = m[0], m[1]
    count = 0


    def dfs(lis, l, count, k):
        if iscontinuity(lis, k, l):
            count += 1
        if len(lis) == l:
            return count
        return dfs(lis + ['r'], l, count, k) + dfs(lis + ['w'], l, count, k)


    all_count = 0
    for i in range(a, b + 1):
        lis = []
        all_count += dfs(lis, i, count, k)
    print(int(all_count%(1e9+7)))
