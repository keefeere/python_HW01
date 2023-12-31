#!/usr/bin/env python3

##################
# Calculator by keefeere(c)2023
##################

# Define functions for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Use try catch to handle zero division
    try:
        return x / y
    except ZeroDivisionError:
        print("\nError: Cannot divide by zero")
        exit()

# Define a function to check if a number is NaN
# from https://towardsdatascience.com/5-methods-to-check-for-nan-values-in-in-python-3f21ddd17eed
def isNaN(num):
    return num != num

# Define a function to format the output
def format_output(result):
    # Check if the result is infinity or NaN
    if result == float("inf") or isNaN(result):
        # Return the result as it is
        return str(result)
    else:
        # Check if the result is an integer
        if result == int(result):
            # Try to return the result as an integer without decimal point
            try:
                return int(result)
            except ValueError:
                # Handle the value error
                return "Error: Cannot convert value to integer"
        else:
            # Return the result as a float with 6 digits before decimal point
            return f"{result:.6f}"  #https://www.geeksforgeeks.org/precision-handling-python/

# Define a function to get and validate a number from the user
def get_number(prompt):
    valid = False
    while not valid:
        try:
            num = float(input(prompt).replace(',', '.'))
            valid = True
        except ValueError:
            print("Error: Please enter a valid number. \nThe program supports only integers written in the decimal number system and decimal fractions with a dot or comma separator")
        except KeyboardInterrupt:
            print("\nExiting the program...")
            exit()
        finally:
            print("Input validation completed") #not needed just for test of finally statement
    return num

# Welcome message
print("Welcome to the Calculator Program by keefeere! \nThe program supports only integers written in the decimal number system and decimal fractions with a dot or comma separator")

# Prompt the user to select an operation
print("\nPlease select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get the user's choice and validate it
valid = False
while not valid:
    try:
        choice = int(float(input("\nEnter your choice (1-4): ").replace(',', '.')))
        if choice in [1, 2, 3, 4]:
            valid = True
        else:
            print("Error: Please enter a valid choice")
    except ValueError:
        print("Error: Please enter a valid choice")
    except KeyboardInterrupt:
        print("\nExiting the program...")
        exit()
    finally:
        print("Choice validation completed")

# Get and validate the first number if the choice is valid
if valid:
    num1 = get_number("Please enter the first number. \nThe number should be an integer written in the decimal number system or decimal fractions with a dot or comma separator: ")

# Get and validate the second number if the first number is valid
if valid:
    num2 = get_number("Please enter the second number. \nThe number should be an integer written in the decimal number system or decimal fractions with a dot or comma separator: ")

# Perform the calculation and display the result if both numbers are valid
if valid:
    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)

    # Format the output and print it with different messages depending on the type of result
    output = format_output(result)
    if isinstance(output, int):   #https://www.geeksforgeeks.org/type-isinstance-python/
        print("\nThe result is:", output)
    else:
        print("\nThe result is rounded to 6 digits:", output)