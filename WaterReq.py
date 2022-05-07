# Input Format
# The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains an integer N, as described in the problem statement.

# Output Format
# For each test case, output the number of liters of water required by the water cooler to cool for N hours

#     Sample
#     Input
#     1
#     2
#     1
#     2
#     Sample
#     Output
#     1
#     2
#     4

# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    print(2*n)
    t=t-1

