### Assignment one, create a list of numbers

# You assignment is to use a while loop to create a list of numbers from 1 to 100. Then use a for loop to iterate over the list and print out each number.
list = []
i = 0
while i < 100:
    i += 1
    list.append(i)
    
for i in list:    
    print(f"No: {i}")

### Assignment two, use a for-loop to iterate over a list

# In this assignment, you'll use a for-loop to iterate over a list of customers and print out each customer name.

customers = ["John", "Mary", "Steve", "Trudy", "Henry"]
for customer in customers:
    print(customer)

### Assignment three, a scientific reader

# You will read input from the user, negative numbers should be discarded. Non numbers should cause an error in the program. The program should keep reading numbers until the user enters a zero. When the user enters a zero, the program should print out the average of all the numbers entered.

user_input = input("Enter a number: ")
numbers = []
while user_input != "0":
    try:
        number = int(user_input)
        if number > 0:
            numbers.append(number)
    except ValueError:
        print("Invalid input")
    user_input = input("Enter a number: ")