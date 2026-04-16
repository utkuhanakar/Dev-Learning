# ============================================================================
# 🐍 PYTHON MASTERCLASS: MODULE 1 - THE BASICS
# ============================================================================
# Welcome! This file represents your interactive Python curriculum.
# Read the English explanations (text starting with #) and examine the code.
# Run this script to see the outputs in your terminal!
#
# 🎯 Module 1 Goals:
#   1. Understanding Comments & Print Statements
#   2. Variables (How to store data)
#   3. Basic Data Types (Text, Numbers, True/False)
# ============================================================================

print("--- SECTION 1: HELLO WORLD & COMMENTS ---")

# This is a comment. Python ignores anything that starts with a hash `#`.
# We use comments to explain our code to other humans (and ourselves!).

# The `print()` function is how we tell Python to show us something on the screen.
print("Hello, World!") 

# Try running this file! You should see "Hello, World!" printed in your console.


print("\n--- SECTION 2: VARIABLES ---")
# Think of a variable as a labeled box where we can store information.
# We create a variable by giving it a name, using an equals sign `=`, 
# and then giving it a value.

player_name = "Arthur"
player_score = 100

print("Player Name:")
print(player_name)

print("Player Score:")
print(player_score)

# We can also change the value stored inside the variable later!
player_score = 150
print("New Player Score:")
print(player_score)


print("\n--- SECTION 3: DATA TYPES ---")
# Python stores different kinds of information differently. 
# Here are the 4 most important basic "Data Types":

# 1. Strings (str): Used for text. Always enclosed in quotes ("" or '').
character_class = "Warrior"

# 2. Integers (int): Whole numbers (no decimals). Can be positive or negative.
level = 5

# 3. Floats (float): Decimal numbers.
health_points = 98.5

# 4. Booleans (bool): Represents True or False. (Notice the capital T and F)
is_game_over = False
has_magic_sword = True

# We can print multiple things at once by separating them with a comma!
print("Status -> Class:", character_class, "| Level:", level, "| HP:", health_points)
print("Is the game over?", is_game_over)


# ============================================================================
# 🛑 END OF MODULE 1 
# ============================================================================
# HOMEWORK / PRACTICE:
# 1. Try changing the `player_name` variable to your own name.
# 2. Add a new variable called `age` and give it your age as an integer.
# 3. Use print() to display your new variable.
#
# Run the code (python Python-Learning.py) to see your results!
# Whenever you are ready to learn more, just tell me: 
# "I am ready for Module 2!"
# ============================================================================
