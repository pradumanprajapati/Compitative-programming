# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases. Then the test cases follow.
# Each test case consists of a single line of input containing three space-separated integers X,Y,Z.

# Sample Input 1
# 4
# 1 2 3
# 10 12 13
# 23 1 22
# 23 1 63
# Sample Output 1
# 2
# 1
# 0
# 2

# cook your dish here
t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    if x + y <= z:
        print(2)
    elif x > z:
        print(0)
    else:
        print(1)



