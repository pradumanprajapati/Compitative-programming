def bin(n):

    i = 1 << 3
    s=""
    while (i > 0):

        if ((n & i) != 0):

            s=s+'1'

        else:
            s=s+'0'

        i = i // 2
    return s
t=input()
l=[]
ans=[]
for i in t:
    if i!=':':
        c=int(i)
        b=bin(c)
        l.append(b)

a=l[0][0]+l[0][1]+l[2][0]+l[3][0]+l[4][0]+l[5][0]
b=l[0][0]+l[1][1]+l[2][1]+l[3][1]+l[4][1]+l[5][1]
c=l[0][0]+l[1][2]+l[2][2]+l[3][2]+l[4][2]+l[5][2]
d=l[0][0]+l[0][1]+l[2][3]+l[3][3]+l[4][3]+l[5][3]

s=0
t=0

for j in range(len(a)):
    i=j
    s=0
    if a[i]!='0':
        while(i<len(a) and a[i]!='0'):
            s+=int(a[i])
            i+=1
    if t<s:
        t=s
print(t,end=",")
s=0
t=0
for j in range(len(b)):
    i=j
    s=0
    if b[i]!='0':
        while(i<len(b) and b[i]!='0'):
            s+=int(b[i])
            i+=1
    if t<s:
        t=s
print(t,end=",")
s=0
t=0
for j in range(len(c)):
    i=j
    s=0
    if c[i]!='0':
        while(i<len(c) and c[i]!='0'):
            s+=int(c[i])
            i+=1
    if t<s:
        t=s
print(t,end=",")
s=0
t=0
for j in range(len(d)):
    s=0
    i=j
    if d[i]!='0':
        while(i<len(d) and d[i]!='0'):
            s += int(d[i])
            i += 1
    if t<s:
        t=s
print(t)