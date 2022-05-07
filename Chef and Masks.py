# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases. Then the test cases follow.
# Each test case consists of a single line of input, containing two space-separated integers X,Y.

# Sample Input 1
# 4
# 10 100
# 9 100
# 88 99
# 1 11
# Sample Output 1
# Cloth
# Disposable
# Cloth
# Disposable

# cook your dish here
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if x * 100 < y * 10:
        print("Disposable")
    else:
        print("Cloth")
