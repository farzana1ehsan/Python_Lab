'''4. Write a program that counts:
• Number of even elements
• Number of odd elements
in a list'''

ListOfNumbers=[]
x=int(input("How many numbers you want to enter: "))
for i in range(x):
    number=int(input(f"Enter the {i} number: "))
    ListOfNumbers.append(number)

countEven=0
countOdd=0
for number in ListOfNumbers:
    if number %2==0:
        countEven+=1
    else:
        countOdd+=1
print("Number of Even Numbers: ",countEven)
print("Number of Odd Numbers: ",countOdd)