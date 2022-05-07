# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases. Then the test cases follow.
# Each test case consists of a single line of input, containing a single integer N

# Sample Input 1
# 4
# 2
# 3
# 4
# 9
#
# Sample Output 1
# 3
# 3
# 6
# 12

# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    print((n//2)*3)