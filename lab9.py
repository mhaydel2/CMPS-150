# Author:         Milan Haydel
# ULID/Section:   C00419477 / CMPS 150-002

# open data file
infile = open("bookData.py", "r")

print()
print("Region     Fiction     Non-Fiction      Total         Tax      Total Sales")
print("--------------------------------------------------------------------------")

# initialize sums
finalTotalSales = 0
totalFiction = 0
totalNonFiction = 0

# read first set of data
region = infile.readline().strip()
fiction = eval(infile.readline())
nonFiction = eval(infile.readline())
taxRate = eval(infile.readline())

#initialize the minimums and maximums (both the number and the region)
maxFiction = fiction
minNonFiction = nonFiction
maxRegion = region
minRegion = region
  
  
while region != "XX":

    # compute values needed for table
    total = fiction * 14.95 + nonFiction * 9.95
    tax = total * taxRate
    totalSales = total + tax

    # print entry in table          
    print(format(region,'>4s'),format(fiction,'12d'),format(nonFiction,'12d'),
          format(total,'15.2f'),
          format(tax,'12.2f'),
          format(totalSales,'14.2f'))
   
    # update sums
    finalTotalSales = finalTotalSales + totalSales
    totalFiction = totalFiction + fiction
    totalNonFiction = totalNonFiction + nonFiction

    # update (if needed) min & max
    # notice that it is two separate if statements
    
    if fiction > maxFiction:
        maxFiction = fiction
        maxRegion = region
            
    if nonFiction < minNonFiction:
        minNonFiction = nonFiction
        minRegion = region

    
    # get the next set of data
    region = infile.readline().strip()
    fiction = eval(infile.readline())
    nonFiction = eval(infile.readline())
    taxRate = eval(infile.readline())


infile.close()

# print summary statistics
print("--------------------------------------------------------------------------")
print("Total",format(totalFiction,'11d'),
      format(totalNonFiction,'12d'),format(" ",'>31s'),
      format(finalTotalSales,'11.2f'))
print()
print("Region with MAX Fiction:")
print(format(maxRegion,'>4s'),format(maxFiction,'12d'))
print()
print("Region with MIN NonFiction:")
print(format(minRegion,'>4s'),format(minNonFiction,'12d'))
print()



