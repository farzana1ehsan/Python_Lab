'''
3. Given a list of integers, calculate:
• Sum
• Average
• Maximum value
• Minimum value
without using built-in functions such as sum(), max(), or min().'''

#from numpy import maximum


ListOfNumbers=[]
x=int(input("How many numbers you want to enter: "))
for i in range(x):
    number=int(input(f"Enter the {i} number: "))
    ListOfNumbers.append(number)
sumOfnumbers=0
maxValue=ListOfNumbers[0]
minValue=ListOfNumbers[0]

for i in ListOfNumbers:
    sumOfnumbers+=i
    if i>maxValue:
        maxValue=i
    if i<minValue:
        minValue=i
avg=sumOfnumbers/len(ListOfNumbers)

print("Total: ",sumOfnumbers)
print("Average: ",avg)
print("Maximum: ",maxValue)
print("Minimum: ",minValue) 

