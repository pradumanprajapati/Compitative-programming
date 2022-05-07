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

# cook your dish here
t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    if y-x>2*z:
        print("NO")
    else:
        print("YES")