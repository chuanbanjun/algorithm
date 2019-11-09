import sys

# 不定行输入
try:
    while True:
        line =  sys.stdin.readline().strip()
        if line == '':
            break
        a = list(map(int,(line).split(' ')))
except:
     pass


# 多行输入
import sys

# 读取第一行的n
n = int(sys.stdin.readline().strip())
for i in range(n):
    line = sys.stdin.readline().strip()
    # 每一行数字分隔后转化成int列表
    values = list(map(int, line.split()))


# 输入为二维矩阵
matrix = []
for i in range(n):
    matrix.append(list(map(int,input().split())))

