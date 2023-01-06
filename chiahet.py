import sys
sys.stdin = open('CHIAHET.INP','r')
sys.stdout = open('CHIAHET.OUT','w')
n , m = map(int,input().split())
t = 1
for i in range(1,n+1):
    t *= i
for i in range(99999):
    res = pow(m,i)
    if t % res == 0 and t % (res - 1) != 0:
        print(i)