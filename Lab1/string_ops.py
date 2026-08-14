# Demonstrates string manipulation and built-in string methods

full_name = input("Enter your full name: ")

print("Uppercase:", full_name.upper())  # Method 1
print("Lowercase:", full_name.lower())  # Method 2
print("Title Case:", full_name.title())  # Method 3
print("Reversed:", full_name[::-1])  # Extended slicing syntax
print("Length:", len(full_name))