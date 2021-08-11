print("Welcome to Astrologer's Stars\nHow many rows you want?")
numbers_of_rows=int(input())
print("Type 0 or 1")
pattern_style=int(input())
boolean=bool(pattern_style)
if boolean==True:
    for i in range(1,numbers_of_rows+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif boolean==False:
    for i in range(numbers_of_rows,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

