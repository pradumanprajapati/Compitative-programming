import math
n = int(input())
l2=[]
for i in range(n):
    l1= list(map(int,input().split(",")))
    l2.extend([l1])
m = int(input())
def sumOfKxKMatrices(arr:list, k:int):
    n = len(arr)

    ans = [[0 for i in range(n-k+1)] for j in range(n-k+1)] 

    for i in range(n-k+1):
        for j in range(n-k+1):
            sm = 1
            for x in range(k):
                for y in range(k):
                    sm *= arr[x + i][y + j]
            ans[i][j] = sm
    return ans

t=sumOfKxKMatrices(l2,m)
l2=[]
l3=[]
for i in range(len(t)):
    for j in range(len(t[i])):
        if (math.ceil(math.sqrt(t[i][j])) ==math.floor(math.sqrt(t[i][j]))):
            l2.append(t[i][j])
        else:
            l3.append(t[i][j])
l3=l3[::-1]
l2.extend(l3)
for i in range(len(l2)):
    if i != len(l2)-1:
        print(l2[i],end=",")
    else:
        print(l2[i])