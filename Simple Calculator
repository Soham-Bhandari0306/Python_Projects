print("Simple Calculator")

print("Choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1/2/3/4): ")

# Ask how many numbers user wants to calculate
count = int(input("How many numbers do you want to calculate? "))

numbers = []

# Take numbers from user
for i in range(count):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Perform calculation
if choice == '1':  # Addition
    result = sum(numbers)
    print("Result:", result)

elif choice == '2':  # Subtraction
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    print("Result:", result)

elif choice == '3':  # Multiplication
    result = 1
    for num in numbers:
        result *= num
    print("Result:", result)

elif choice == '4':  # Division
    result = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            print("Error: Division by zero is not allowed")
            break
        result /= num
    else:
        print("Result:", result)

else:
    print("Invalid choice")
