#  Author:          Milan Haydel
#  ULID/Section:    C00419477 / CMPS 150
#  lab11.py 

import random

def main():
    # create an empty list
    list1 = []
    count = 0
    # set up a counting loop to append 15 random integers
    # to the list, ranging from 1 to 25 (inclusive)
    while count < 15:
        num = random.randint(1,25)
        list1.append(num)
        count += 1

    # print the list
    print(list1)

    # generate one more random integer in the same range
    # append it to list ONLY IF it is not already in the list
    # you are NOT allowed to use the builtin method/function 'in' or 'not in'
    list3 = random.randint(1,25)
    if list3 != len(list1):
        print("newInt = ", list3)
        print(list3, " is NOT in the list ... it has been added!")
        list1.append(list3)
        print(list1)
        # call function to swap and reverse list
        numSwap(list1, 15)
    else:
        print("newInt = ", list3)
        print(list3, " is already in the list ... not added!")
        print(list1)
        # call function to swap and reverse list
        numSwap(list1, 14)
    print(len(list1))

    
# function to swap and reverse list
def numSwap(list1, end):
    list1[0], list1[end] = list1[end], list1[0]
    print(list1)
    list1.reverse()
    # print the list
    print(list1)

main()
