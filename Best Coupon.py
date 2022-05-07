# Input Format
#
# The first line contains a single integer T - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains a single integer X - the bill amount before discount.
#
# Sample Input 1
# 3
# 300
# 1300
# 1000
#
# Sample Output 1
# 100
# 130
# 100

# cook your dish here
t=int(input())
for _ in range(t):
    x=int(input())
    count=max(x//10,100)
    print(count)
