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
        return "Error: Cannot divide by zero"

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
            num = float(input(prompt))
            valid = True
        except ValueError:
            print("Error: Please enter a valid number")
        except KeyboardInterrupt:
            print("\nExiting the program...")
            break
        finally:
            print("Input validation completed")
    return num

# Welcome message
print("Welcome to the Calculator Program by keefeere!")

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
        choice = int(input("\nEnter your choice (1-4): "))
        if choice in [1, 2, 3, 4]:
            valid = True
        else:
            print("Error: Please enter a valid choice")
    except ValueError:
        print("Error: Please enter a valid choice")
    except KeyboardInterrupt:
        print("\nExiting the program...")
        break
    finally:
        print("Choice validation completed")

# Get and validate the first number if the choice is valid
if valid:
    num1 = get_number("Please enter the first number: ")

# Get and validate the second number if the first number is valid
if valid:
    num2 = get_number("Please enter the second number: ")

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
        print("\nThe result is an integer:", output)
    elif isinstance(output, float):
        print("\nThe result is a float rounded to 6 digits:", output)
    else:
        print("\nThe result is:", output)
