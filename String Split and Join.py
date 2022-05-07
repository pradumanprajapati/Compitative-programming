
# create of the def function of the program
def swap_case(s):
    t = " "  # Output secton
    for i in s:
        # Condition of the upper function with the Output
        if (i.isupper() == True):
            # Lower of the Output section
            t += (i.lower())
        elif (i.islower() == True):
            # upper string of the Output
            t += (i.upper())
        else:
            t += i
            # create of the return function
    return t
    # create of the Condition of result in the def function with the Condition


if __name__ == '__main__':
    # create of input condition with inputof user define function
    s = input()
    # A resultof the swap_caseof ther string in the swap_case
    result = swap_case(s)
    # finally of the swap_case in the result of Output
    print(result)


