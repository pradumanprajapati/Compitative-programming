# Input:
# First line will contain T, number of testcases. Then the testcases follow.
# Each testcase contains a single line of input, three integers x,m,d

# Sample Input 1
# 3
# 1 1 0
# 1 3 1
# 2 2 3
# Sample Output 1
# 1
# 2
# 4

# cook your dish here
t=int(input())
for _ in range(t):
    x,m,d=map(int,input().split())
    v=min(x*m ,d+x)
    print(v)