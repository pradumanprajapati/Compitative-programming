# Input Format
# The first line of input contains a single integer T denoting the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains three space-separated integers SA,SB,SC, denoting the number of successful submissions of problems A,B,C respectively.

# Sample Input 1
# 3
# 1 4 2
# 16 8 10
# 14 15 9
# Sample Output 1
# Draw
# Bob
# Alice


# coding your disk here
t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    if (c<a and c<b):
        print("Alice")
    elif (b<a and b<c) :
        print("Bob")
    else:
        print("Draw")


