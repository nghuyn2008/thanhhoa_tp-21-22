import sys
sys.stdin = open('DIV3.INP','r')
sys.stdout = open('DIV3.OUT','w')
n = int(input()) 
a =[int(i) for i in input().split()]
li =[]
for i in range(len(a)):
    for j in range(i,len(a)):
        if (a[i] + a[j]) % 3 == 0:
            li.append(i)
            li.append(j)
print(len(li) //2)