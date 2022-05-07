def rotate(l, n):
    res = l[len(l) - n:len(l)] + l[0:len(l) - n]
    return res


m = (int)(input())
mat = []
for i in range(m):
    l = (list)(map(str, input().split()))
    mat.append(l)
ans = []
# print(mat)
res = []
for i in range(m):
    r = (str)(mat[i])
    s = r[2:len(r) - 4]
    nr = r[len(r) - 3:len(r) - 2]
    vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    nr = (int)(ord(nr) - 48)

    k = rotate(s, nr)
    # print(k)

    x = ''
    for j in range(len(k)):
        if k[j] not in vow and (j + 1) % 2 == 0:
            x = x + k[j]
    res.append(x)
c = 0
for i in res:
    if len(i) == 0:
        c += 1
if c == len(res):
    print("-1")
else:
    k = []
    if len(res) > 0:
        for i in res:
            if len(i) == 0:
                pass
            else:
                k.append(i)
        k = sorted(k, key=len)
        ans = ''
        for i in k:
            ans = ans + i + ','
        print(ans[0:len(ans) - 1])