
1. Variable and Identifier Practice (variable_practice.py)
   Aim: Store basic user information in variables of appropriate data types and print them along with their types.
   Logic: Assign values to variables for name, age, height, and student status. Pass each variable into the type() function inside print() statements to verify and display their data types.
   Sample Input / Output:
     Input: None
     Output:
       Name: Harsh <class 'str'>
       Age: 21 <class 'int'>
       Height: 5.9 <class 'float'>
       Is Student: True <class 'bool'>

2. Greeting Program (greeting.py)
   Aim: Take user details as input and generate a formatted greeting sentence.
   Logic: Collect the user's name, age, and city using the input() function. Combine these variables into a single sentence using f-string formatting and print the output.
   Sample Input / Output:
     Input:
       Enter your name: Johny
       Enter your age: 20
       Enter your city: Indore
     Output: Hello Johny, you are 20 years old and live in Indore.

3. Arithmetic Operations (arithmetic_ops.py)
   Aim: Perform standard mathematical operations on two user-provided numbers.
   Logic: Prompt for two numbers and convert them to floats. Calculate their sum, difference, product, quotient, and remainder, incorporating a safety check to prevent zero division errors.
   Sample Input / Output:
     Input:
       Enter first number: 10
       Enter second number: 4
     Output:
       Sum: 14.0
       Difference: 6.0
       Product: 40.0
       Quotient: 2.5
       Remainder: 2.0

4. Celsius to Fahrenheit (temp_converter.py)
   Aim: Convert a temperature value given in Celsius to Fahrenheit.
   Logic: Take the temperature input in Celsius and convert the string input to a float. Apply the conversion formula (C * 9/5) + 32 and display the final temperature.
   Sample Input / Output:
     Input:
       Enter temperature in Celsius: 25
     Output: 25.0C is equal to 77.0F

5. String Manipulation (string_ops.py)
   Aim: Demonstrate common string operations and transformations on a input string.
   Logic: Read a full name string from the user. Apply built-in methods .upper(), .lower(), and .title() for case changes, string extended slicing [::-1] for reversing, and len() to calculate total character length.
   Sample Input / Output:
     Input:
       Enter your full name: John Doe
     Output:
       Uppercase: JOHN DOE
       Lowercase: john doe
       Title Case: John Doe
       Reversed: eoD nhoJ
       Length: 8

6. Escape Sequence Practice (receipt.py)
   Aim: Format tabular text output cleanly using control characters.
   Logic: Store itemized details in a single string variable. Use tab characters (\t) to space out columns evenly and newline characters (\n) to break rows into a clean receipt layout.
   Sample Input / Output:
     Input: None
     Output:
       ITEM		QTY	PRICE
       -----------------------------
       Coffee		2	$7.00
       Sandwich	1	$8.50
       -----------------------------
       TOTAL			$15.50

7. Calculator (calculator.py)
   Aim: Run an interactive menu-driven calculator until the user chooses to exit.
   Logic: Set up a while loop that displays menu choices and prompts for selection. Perform the selected mathematical operation on two numbers or break the loop when the exit option is selected.
   Sample Input / Output:
     Input:
       Select an option (1-5): 1
       Enter first number: 8
       Enter second number: 2
       Select an option (1-5): 5
     Output:
       Result: 10.0
       Exiting calculator.