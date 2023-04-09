# Author: Norm McCord
# Date Created: 20230408
# Date Last Modified: 20230408
# Purpose: Demonstrate exceptions with a calculator program, create custom exceptions

# Write an interactive calculator! User input is assumed to be a formula that consists of a number, an operator (+, -, *, /), and another number, separated by white space

# (input validation)
# If input doesn't consist of 3 elements, raise a FormulaError, which is a custom Exception'
# Try to convert the first and third input into a float.  Report and invalid inputs and what they were
# If the second input is not +, -, *, /, raise a FormulaError
# If the input is valid, perform the calculation and print the result

# Define formula error
class FormulaError(Exception):
    pass

n1 = None; n2 = None

# User input
formula = input("Enter a formula: ")

# Input validation
tokens = formula.split(" ") # split string on a single space
# print(tokens)

# Try; except; else
try:
    if len(tokens) != 3:
        raise FormulaError

    n1 = float(tokens[0])
    n2 = float(tokens[2])

    if tokens[1] != '+' and tokens[1] != '-' and tokens[1] != '*' and tokens[1] != '/':
        raise FormulaError
except FormulaError:
    print("Error in formula")
except ValueError:
    print("The formula contained a number which cannot be turned into a float.")
    print(formula)

else:
    # Perform calculations
    if n1 != None and n2 != None:
        if tokens[1] == "+":
            print(n1 + n2)
        elif tokens[1] == "-":
            print(n1 - n2)
        elif tokens[1] == "*":
            print(n1 * n2)
        elif tokens[1] == "/":
            print(n1 / n2)
