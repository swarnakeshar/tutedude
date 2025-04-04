# Take 2 numbers as input form user

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform basic math operations

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Display the results (Rounded to one decimal place)

print("Addition: ", addition.__round__(1))
print("Subtraction: ", subtraction.__round__(1))
print("Multiplication: ", multiplication.__round__(1))
print("Division: ", division.__round__(1))