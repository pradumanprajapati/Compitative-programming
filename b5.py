#  Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
data = input("enter numbers \n ")
list = data.split(",")
tuple = tuple(list)
print('Li : ',list)
print('Tuple : ',tuple)