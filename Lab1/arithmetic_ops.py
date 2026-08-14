# Performs basic arithmetic operations on two user-input numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
# Ternary operator checks for zero division
if num2==0:
    print("Quotient and Remainder cant be checked as num2 is 0")
else:    
    print(f"Quotient: {num1 / num2}")
    print(f"Remainder: {num1 % num2}")

