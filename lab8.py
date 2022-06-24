# Author:         Milan Haydel
# ULID/Section:   C00419477 CMPS 150-002
# Lab #8
 
infile = open("fuel.py","r")
    
print()
print("    Fuel Type        Gallons     Bill")
print("-------------------------------------")

totalGallons = 0
totalBill = 0
count = 0

fuelType = infile.readline().strip()
amount = eval(infile.readline()) 
              
while amount != 0:
    if fuelType == 'S':
         word = "Regular Unleaded"
         bill = amount * 2.62
    elif fuelType == 'P':
         word = "Unleaded Plus"
         bill = amount * 2.36
    elif fuelType == 'R':
         word = "Regular Unleaded"
         bill = amount * 2.12
    elif fuelType == 'D':
         word = "Diesel"
         bill = amount * 2.35

    # print each line of output
    print(format(word,'20s'),format(amount,'7.2f'),format(bill,'8.2f'))

    totalGallons = totalGallons + amount
    totalBill = totalBill + bill
    count = count + 1

    fuelType = infile.readline().strip()
    amount = eval(infile.readline()) 
    

infile.close()

print("-------------------------------------")
print(format("Total",'20s'),format(totalGallons,'7.2f'),format(totalBill,'8.2f'))
print()

averageGallons = totalGallons / count
averageBill = totalBill / count

print("Average Gallons:",format(averageGallons, '7.2f'))
print("Average Bill:   ",format(averageBill, '7.2f'))

