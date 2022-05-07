# Input : mylist = [23, 65, 19, 90], pos1 = 0, pos2 = 2
# Output : [19, 65, 23, 90]
#
# Input : mylist = [1, 2, 3, 4, 5], pos1 = 1, pos2 = 4
# Output : [1, 5, 3, 4, 2]
#fast program
# def swapmylist(mylist):
#     mylist[0],mylist[2]=mylist[2],mylist[0]
#     return mylist
# mylist=[23,65,19,90]
# print(swapmylist(mylist))

# program scound method pop and instert
def swapmylist(mymylist, pos1, pos2):
    # delete elements from mylist
    first_ele = mylist.pop(pos1)
    second_ele = mylist.pop(pos2 -1)

    # inserting value in changing positions
    mylist.insert(pos1, second_ele)
    mylist.insert(pos2, first_ele)

    return mylist

mylist = [1, 5, 3, 4, 2]
pos1, pos2 = 1, 4
print(swapmylist(mylist, pos1 , pos2 ))