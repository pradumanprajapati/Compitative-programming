# Input Format:
# First line will contain T, number of testcases. Then the testcases follow.
# Each testcase contains of a single line of input, three integers  X,Y,Z

# Sample Input 1
# 3
# 4 10 8
# 3 6 1
# 4 8 2
# Sample Output 1
# YES
# NO
# YES

t=int(input())
for _ in range(t):
    n,x,p=map(int,input().split())
    if (x*3-(n-x))>=p:
        print("PASS")
    else:
        print("FAIL")