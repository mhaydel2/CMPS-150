# Author:         Milan Haydel
# ULID/Section:   C00419477 / CMPS 150-002
# Lab #7
 

# this is a count-controlled loop

sumGallons = 0


for i in range(3):
    # read and process data
    fuelType = input("Enter fuel type: ")
    gallons = eval(input("Enter fuel amount: "))

    if fuelType == 'S':
        word = "Super Unleaded"
        bill = 2.62 * gallons
    elif fuelType == 'P':
        word = " Unleaded Plus"
        bill = 2.36 * gallons
    elif fuelType == 'R':
        word = "Regular Unleaded"
        bill = 2.12 * gallons
    elif fuelType == 'D':
        word = "Diesel"
        bill = 2.35 * gallons
        


    sumGallons = gallons + sumGallons

    print(format(" ",'25s'),format(word,'20s'),format(gallons,'7.2f'),
          format(bill,'8.2f'))


print()
print("Total Gallons:",sumGallons)
print()
