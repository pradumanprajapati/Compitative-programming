# Input Format
# The first line contains an integer T denoting the number of test cases. T test cases then follow.
# The first and only line of each test case contains 3 space separated integers M, N and K.

# Sample Input 1
# 3
# 10 1 10
# 25 2 10
# 15 2 10
# Sample Output 1
# NO
# YES
# NO

t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    if m>n*k:
        print("Yes")
    else:
        print("No")

