# Author:         Milan Haydel
# ULID/Section:   C00419477 / CMPS 150-002
# Lab #12

def main():
    infile = open("lab12data.py", "r")

    housewaresList = []
    clothingList = []
    groceryList = []

    # read first data set
    category = infile.readline().strip()
    count = eval(infile.readline())

    while category != "END":

        # add the count data item to the appropriate list
        if category == "Housewares":
            housewaresList.append(count)
        elif category == "Clothing":
            clothingList.append(count)
        else:
            groceryList.append(count)

        # read first data set
        category = infile.readline().strip()
        count = eval(infile.readline())

    infile.close()

    # print all 3 lists, just "as a list"



    # call a function to print the "pretty" table
    PrintPrettyTable(housewaresList,clothingList,groceryList)



def PrintPrettyTable(housewaresList,clothingList,groceryList):
    print("Housewares List: ", housewaresList)
    print("Clothing List:   ", clothingList)
    print("Grocery List:    ", groceryList)
    print()
    print("Category   Count")
    print("----------------")
    for i in range(len(housewaresList)):
        print("Housewares  ",format(housewaresList[i],'>3d'))
    for i in range(len(clothingList)):
        print("Clothing    ",format(clothingList[i],'>3d'))
    for i in range(len(groceryList)):
        print("Grocery     ",format(groceryList[i],'>3d'))

main()
