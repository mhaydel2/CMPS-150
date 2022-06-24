# sample solution  --  lab11.py 

import random

def main():
    intList = []

    for i in range(15):
        newInt = random.randint(1,25)
        intList.append(newInt)

    '''   # this is a while loop using count control
    count = 0
    while count < 15:
        newInt = random.randint(1,25)
        intList.append(newInt)
        count = count + 1
    '''
    
    # print the list
    print(intList)

    # generate a new number to possibly add to the list
    newInt = random.randint(1,25)
    print("\nnewInt =",newInt)
    
    # code to append if not in the list, using a loop
    found = False
    for i in range(len(intList)):
        if intList[i] == newInt:
            found = True
    if found == False:
        intList.append(newInt)
        print(newInt, "is NOT in the list ... it has been added!")
    else:
        print(newInt, "is already in the list ... not added!")

    '''
    # this is what is NOT allowed 
    # code to append if not in the list. using the "not in" statement
    if newInt not in intList:
        intList.append(newInt)
    '''

    # print the list
    print()
    print(intList)
    print()
    
    SwapFirstLast(intList)
    print(intList)
    reverseInts = Reverse(intList)
    print(reverseInts)
        
def SwapFirstLast(nums):
    temp = nums[0]
    nums[0] = nums[len(nums)-1]
    nums[len(nums)-1] = temp

def Reverse(nums):
    reverse = []
    for i in range(len(nums)-1,-1,-1):
        reverse.append(nums[i])
    return reverse

main()
