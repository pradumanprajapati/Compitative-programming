def max(a,b):
    if a>=b:
        return a
    else:
        return b
a,b=map(int,input("enter the number\n").split())
print(max(a,b))