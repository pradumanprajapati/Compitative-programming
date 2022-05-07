# Input Format

# The first line contains a single integer T - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains two integers X and Y - the cost of a double room and the cost of a triple room.

# Sample Input 1
# 3
# 10 15
# 6 8
# 4 8

# Sample Output 1
# 30
# 16
# 12

# cook your dish here
t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    count=min(3*x,2*y)
    print(count)