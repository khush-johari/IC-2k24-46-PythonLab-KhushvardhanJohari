# Converts temperature input from Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32  # Conversion formula

print(f"{celsius}C is equal to {fahrenheit}F")