
n=input()
n1=int (n)
new=n[:]
ans=[]
a=1
for i in range(len(n)):
    s=0
    n1=int (new)
    for k in range(len(n)):
        n1=int (new)
        s=s*10+int(new[k])
        if n1%s==0:
            ans.append(s)

    if a==len(n):
        break
    new=n[a:]+n[:a]
    a+=1
ans.sort()
for i in range(len(ans)):
    if i!=len(ans)-1:
        print (ans[i], end=',')
    else:

        print (ans[i])