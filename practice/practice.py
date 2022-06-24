inp = input("Enter a string with only I,V,X: ")
Sum = 0
num = 0
for i in range len(inp):
    while num <= len(inp):
        if inp[i] == 'I':
            Sum = Sum + 1
            num += 1
        elif inp[i] == 'V':
            Sum = Sum + 5
            num += 1
        elif inp[i] == 'X':
            Sum = Sum + 10
            num += 1

print(Sum)
