import sys
sys.stdin = open('GHH.INP','r')
sys.stdout = open('GHH.OUT','w')
n = int(input())
a = [] ; li = [] ; count = 0
for _ in range(n):
    a.append(int(input()))
for i in range(len(a)):
    t = a[i]
    l =[]
    for j in range(1 , t + 1):
        if t % j == 0:
            l.append(j)
        if 2 * t <= sum(l):
            count += 1
            li.append(t)
print(count)
for i in range(len(li )):
    print(li[i])
