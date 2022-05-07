# Input Format
#
# The first line will contain T, the number of test cases. Then the test cases follow.
# Each test case consists of a single line of input, containing three space-separated integers X,Y, and Z.
#
# Sample Input 1
# 3
# 1 1 1
# 2 1 2
# 1 2 3
#
# Sample Output 1
# 1
# 4
# 6

t=int(input())
for _ in range(t):
    x,y,z=map(int,input().split())
    count=x*y*z
    print(count)