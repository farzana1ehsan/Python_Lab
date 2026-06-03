'''5. Given a list of integers, create a new list containing only even numbers'''
listOfNumbers=[12,13,55,23,34,45,56,67,78]
evenNumbers=[num for num in listOfNumbers if num % 2 == 0]

print("Even numbers in the list are: ",evenNumbers)
