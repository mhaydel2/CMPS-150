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
    newInt = linearSearch(list1, list3)
    if newInt != -1:
        list1.append(newInt)

    # print the list
    print(list1)
    
    # call function to swap the first & last element, pass the list as a parameter
    min(list1), max(list1) = numSwap(min(list1), max(list1))

    
    # print the list

    # call function to reverse the list, the function must return the reversed list

    # print the list

def linearSearch(list1, list3):
    for i in range(len(list1)):
        if list3 == list1[i]:
            print("newInt = ", list3)
            print(list3, " is NOT in the list ... it has been added!")
            return list3
        else:
            print("newInt = ", list3)
            print(list3, " is already in the list ... not added!")
            return -1

def numSwap(min(list1), max(list1)):
    return max(list1)
    return min(list1)


main()
