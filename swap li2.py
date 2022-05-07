#secound list
def swap(list):
    list[1], list[2] = list[2],list[1]
    return list
# Driver code
list = [1, 2, 3]
print(swap(list))