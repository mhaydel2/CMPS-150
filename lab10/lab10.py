# Author:         Milan Haydel 
# ULID/Section:   C00419477 / CMPS 150-002
# Lab #10

#****************** LAB Average  ******************
def LabAvg(): 

    infile1 = open("lab10_labGrades.py","r")
    numLab = eval(input("How many lab grades are in the file? "))

    print("Lab Grades: ", end='')
    sumLab = 0
    for i in range(numLab):
        grade = eval(infile1.readline())
        sumLab = sumLab + grade
        print(grade,end=' ')   # this is use of the end= mentioned in chapter 3

    print()
    avgLab = sumLab / numLab      # computes avg (number between 1 & 10, because labs are 10 pts)
    return avgLab  

#****************** PA Average  ****************** 
def PaAvg():

    infile2 = open("lab10_paGrades.py","r")
    numPa = eval(input("How many PA grades are in the file? "))

    print("PA Grades: ", end='')
    sumPa = 0
    for i in range(numPa):
        grade = eval(infile2.readline())
        sumPa = sumPa + grade
        print(grade,end=' ')
        
    print()
    avgPa = sumPa / numPa
    return avgPa

    
#****************** EXAM Average  ****************** 
def ExamAvg():

    infile3 = open("lab10_examGrades.py","r")
    numExam = eval(input("How many exam grades are in the file? "))

    print("Lab Grades: ", end='')
    sumExam = 0
    for i in range(numExam):
        grade = eval(infile3.readline())
        sumExam = sumExam + grade
        print(grade,end=' ')
        
    print()
    avgExam = sumExam / numExam
    return avgExam 
 
#****************** MAIN/DRIVER  ******************

def main():

    print()

    # main will call each of your average functions to compute each component
    # of the overall class avg
    
    # provided for you is the call to the function to compute your LAB average
    # the return value is put in the variable labAverage 

    labAverage = LabAvg()

    # now ... add the code to call the PaAvg and ExamAvg functions
    # their return values must be stored in paAverage and examAverage
    
    paAverage = PaAvg()
    examAverage = ExamAvg()

    # provided for you is the code to convert the averages to percentages
    labPct = labAverage / 10         # labs are worth 10 pts
    paPct = paAverage / 100          # programs are worth 100 pts
    examPct = examAverage / 100      # exams are worth 100 pts

    # compute your OVERALL class average using the weights
    # provided on the lab instruction sheet
    overallAverage = .1*labPct + .2*paPct + .7*examPct
    
    # print results
    print()
    print("  Lab Average =", format(labPct*100,'6.2f'), '%')
    print("   PA Average =", format(paPct*100,'6.2f'), '%')
    print(" Exam Average =", format(examPct*100,'6.2f'), '%')
    print("-------------")
    print("Class Average =", format(overallAverage*100,'6.2f'), '%')
    print()

main()
