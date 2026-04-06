"""
Python Midterm Preparation Study File
This file covers all possible topics for the midterm exam with examples.
Written according to PEP8 standards.
"""

# 1. Variables, Expressions, and Statements
x = 5  # Assignment statement
y = 10 + x  # Expression
print(f"y value: {y}")

# 2. Type Conversions
num_str = "100"
num_int = int(num_str)
num_float = float(num_int)
print(f"Types: {type(num_str)} -> {type(num_int)} -> {type(num_float)}")

# 3. User Input
# Note: input() might wait in interactive environments.
# name = input("What is your name? ") 

# 4. Logical Operators & Boolean
a = True
b = False
print(f"a AND b: {a and b}")
print(f"a OR b: {a or b}")
print(f"NOT a: {not a}")

# 5. Conditional Statements & Logical Branching
age = 20
if age < 18:
    print("Underage")
elif age == 18:
    print("Newly an adult")
else:
    print("Adult")

# 6. Functions & Scope
global_var = "I am global"

def greet(name="Guest"):
    """
    Simple greeting function.
    docstring: Explains the purpose of the function.
    """
    local_var = "I am local"
    return f"Hello {name}! {local_var} and {global_var}"

print(greet("User"))

# 7. Returning Multiple Values
def get_coordinates():
    return 10, 20  # Returns as a tuple

x_coord, y_coord = get_coordinates()
print(f"X: {x_coord}, Y: {y_coord}")

# 8. Fixed and Arbitrary Number of Arguments (*args, **kwargs)
def sum_numbers(*args):
    """Takes an arbitrary number of arguments (*args)"""
    total = 0
    for n in args:
        total += n
    return total

print(f"Sum (1,2,3,4): {sum_numbers(1, 2, 3, 4)}")

def create_profile(**kwargs):
    """Named arbitrary arguments (**kwargs)"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name="Ali", surname="Yilmaz", department="CS")

# 9. Lambda Functions
square = lambda n: n * n
print(f"Square of 5: {square(5)}")

# 10. Lists & List Concepts
fruits = ["apple", "pear", "banana"]
fruits.append("strawberry")
print(f"List: {fruits}, Length: {len(fruits)}")
print(f"Slicing: {fruits[1:3]}")

# 11. Dictionaries
data = {"key": "value", "error": "hata"}
print(f"Dictionary value: {data.get('error')}")

# 12. Loops (for, while)
print("For loop:")
for i in range(3):
    print(f"Index: {i}")

# 13. Strings
text = "  Learning Python  "
print(f"Uppercase: {text.upper().strip()}")
print(f"Split: {text.split()}")

# 14. Debugging (Error Handling: try-except-raise)
try:
    # pay = int(input("Numerator: "))
    pay = 10
    payda = 0
    if payda == 0:
        raise ValueError("Denominator cannot be zero!") # Manual error raising
    result = pay / payda
except ZeroDivisionError:
    print("Zero division error!")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Process completed (executed regardless of error).")

# 15. Doctest Example
def add_nums(a, b):
    """
    Adds two numbers.
    >>> add_nums(2, 3)
    5
    >>> add_nums(-1, 1)
    0
    """
    return a + b

# 16. None Type
empty_val = None
if empty_val is None:
    print("This value is empty (None).")

# INCREMENTAL DEVELOPMENT
# This code is written and tested piece by piece.

print("\n--- Preparation Complete! ---")
