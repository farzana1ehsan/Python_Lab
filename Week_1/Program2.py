listOfNumbers=[]
for i in range (1,11):
    num=int(input(f"Enter the{i}th number: "))
    listOfNumbers.append(num)

print(listOfNumbers)
print("total num of the list",len(listOfNumbers))