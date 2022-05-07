# Why do we need Function_stduyfever
# Factorial N!/ R!(N-N)! Fromula of the code impliment with Python
# usisng of the simple method of the Factorial implimation in Python
# Create of the input function with the variable of the N and R function
n = int(input())
r = int(input())

# Create of the function with the For Loop of the Implimation in the code
# create of the N variable of the implimation code of the function
n_fact = 1
for i in range(1, n + 1):
    n_fact = n_fact * i

# Create of the function with the secound For Loop of the Implimation in the code
# create of the R variable of the implimation code of the function
r_fact = 1
for i in range(1, r + 1):
    r_fact = r_fact * i


# Create of the function with the For Loop of the Implimation in the code
# create of the N-R variable of the implimation code of the function
n_r_fact = 1
for i in range(1, n - r + 1):
    n_r_fact = n_r_fact * i
ans = n_fact // (r_fact * n_r_fact)
print(ans)


