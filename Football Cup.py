# The match ends in a draw, and,
# At least one goal has been scored by either team.
# Given the goals scored by both the teams as X and Y respectively, determine whether Chef will like the match or not.
#
# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases. The description of T test cases follows.
# Each test case consists of a single line of input containing two space-separated integers X and Y — the goals scored by each team.

# Sample Input 1
# 4
# 1 1
# 0 1
# 0 0
# 2 2
# Sample Output 1
# YES
# NO
# NO
# YES

# Codes:

# cook your dish here
t= int(input())
while t > 0:
    m,n = map(int, input().split())
    if (m > 0 and n > 0):
        if (m == n):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    t= t- 1