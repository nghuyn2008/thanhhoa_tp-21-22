import sys
sys.stdin = open('DIFFSSTR.INP','r')
sys.stdout = open('DIFFSSTR.OUT','w')
n = int(input())
s = input()
l = []
for i in range(n):
    for j in range(i , n):
        if j + i < n:
            t = s[i : j]
            l.append(t)
res = -9999
for i in range(len(l)):
    r = len(l[i])
    if r > res:
        res = r
print(res)
