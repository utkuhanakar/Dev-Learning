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
# ============================================================================
# 🌟 STUDENT'S WORK (UTKU) - PERFECTLY DONE! 🌟
# ============================================================================
# Notes from the Professor (AI Agent):
# Excellent job! You correctly defined the variables and successfully 
# displayed them using the print() function. 
# You are officially writing Python code! Keep this here as a memory.
# ============================================================================
player_name = "Utku"
player_age = 19
print("Player Name:", player_name)
print("Player Age:", player_age)


# ============================================================================
# 🐍 PYTHON MASTERCLASS: MODULE 2 - MATH, OPERATORS & STRING FORMATTING
# ============================================================================
# 🎯 Module 2 Goals:
#   1. Understanding basic and advanced mathematical operators.
#   2. Learning how variables are updated in memory.
#   3. F-Strings: The modern, professional way to print text in Python.
#
# 🧠 UNIVERSITY LEVEL INSIGHT:
# In Python, variables are "references" (pointers) to objects in memory (RAM).
# When you do `age = 19`, Python creates an integer object `19` in memory, 
# and the name `age` points to it. This is why Python is dynamically typed!
# ============================================================================

print("\n--- SECTION 1: BASIC MATHEMATICS ---")
# Python is an incredibly powerful calculator. Data Scientists and Game 
# Developers use these operators constantly to calculate physics or analyze data.

gold_coins = 50
silver_coins = 120

# Addition (+) and Subtraction (-)
total_coins = gold_coins + silver_coins
print("Total Coins:", total_coins)

# Multiplication (*) and Division (/)
# IMPORTANT: Division (/) ALWAYS creates a Float (decimal number), even if it divides perfectly!
half_gold = gold_coins / 2  
print("Half of gold coins:", half_gold)  # Prints 25.0, not 25


print("\n--- SECTION 2: ADVANCED MATH OPERATORS ---")
# These are the ones professionals use to solve specific logic problems.

# 1. Floor Division (//): Divides and throws away the decimal part (rounds down).
# Useful in Game Dev for dividing grid cells where you can't have "half a pixel/cell".
steps = 100 // 3 
print("Floor Division (100 // 3):", steps) # Prints 33

# 2. Modulo (%): Returns ONLY the remainder of a division.
# Extremely important in programming! We use % to check if a number is Even or Odd, 
# or to cycle through a list over and over in Animations/UI.
remainder = 10 % 3
print("Modulo (10 % 3):", remainder) # Prints 1, because 10 = (3*3) + 1

# 3. Exponentiation (**): Power of a number (x to the power of y).
# Used in AI / Machine Learning formulas (like calculating Exponential Decay).
power = 5 ** 2 
print("5 to the power of 2 (5 squared):", power) # Prints 25


print("\n--- SECTION 3: UPDATING VARIABLES ---")
# Variables can be updated based on their old value!
experience_points = 100

# Let's say we defeat a monster and gain 50 XP. We can redefine the variable:
experience_points = experience_points + 50
print("XP after monster:", experience_points)

# PROFESSIONAL SHORTCUT:
# Programmers are lazy (in a good way!). Instead of writing `x = x + 50`, we use `+=`.
# This is called an "Assignment/Increment Operator".
experience_points += 50  
print("XP after another monster:", experience_points)
# It works with all operators: -=, *=, /=


print("\n--- SECTION 4: F-STRINGS (MODERN PYTHON MAGIC) ---")
# Before 2016 (Python 3.6), printing mixed text and variables was annoying.
# You used commas like: print("My name is", player_name, "and I am", player_age)
# Now, we use "f-strings" (Formatted String Literals).
# Just put an 'f' before the quotes, and wrap variables in curly braces {}.

# This makes your code infinitely more readable, just like a fill-in-the-blank template!
welcome_message = f"Welcome back, {player_name}! You have {experience_points} XP."
print(welcome_message)

# You can even do math directly inside the curly braces!
print(f"In 5 years, {player_name} will be {player_age + 5} years old.")


# ============================================================================
# 🛑 END OF MODULE 2 
# ============================================================================
# HOMEWORK / PRACTICE:
# 1. Create two new variables: `price` (e.g. 150) and `discount` (e.g. 20).
# 2. Calculate the `final_price` by subtracting the discount from the price.
# 3. Use an f-string to print: "The item costs [Y] dollars." (replace Y with variable)
# 4. Create an `is_even` boolean variable. Use Modulo (`% 2`) on final_price to check
#    if it's perfectly divisible by 2. (Hint: if remainder is 0, it's even!)
#
# When you complete and run your homework, let me know!
# ============================================================================
price = 150
discount = 20
final_price = price - discount
print(f"The item costs {final_price} dollars.")

is_even = final_price % 2 == 0
if is_even == True:
    print("The final price is even.")
else:
    print("The final price is odd.")


# ============================================================================
# 🐍 PYTHON MASTERCLASS: MODULE 3 - CONTROL FLOW & DECISIONS
# ============================================================================
# 🎯 Module 3 Goals:
#   1. Making decisions with if, elif, and else.
#   2. Understanding Conditional Operators (>, <, ==, !=).
#   3. Using Logical Operators (and, or, not).
#
# 🧠 UNIVERSITY LEVEL INSIGHT:
# In programming, "Control Flow" is how your program decides which lines of code
# to execute. Think of it like a train traveling on tracks. "If" statements are 
# the track switches. When a condition is True, the train takes one path; if False,
# it takes another. This is the foundation of ALL Artificial Intelligence (AI)!
# ============================================================================

print("\n--- SECTION 1: IF, ELIF, AND ELSE ---")
# Python uses indentation (spaces at the start of a line) to know which code 
# belongs inside the 'if' block. Other languages use { }, but Python forces 
# you to write clean, readable code vertically.

player_hp = 45

if player_hp > 80:
    print("Player is incredibly healthy!")
elif player_hp > 30:
    # 'elif' stands for "else if". It only runs if the first 'if' was False.
    print("Player is wounded, but okay.")
else:
    # 'else' catches everything else if all previous conditions were False.
    print("WARNING: Player is near death! Use a potion!")


print("\n--- SECTION 2: COMPARISON OPERATORS ---")
# We compare values to create Booleans (True / False).
boss_level = 10
player_level = 10

# Equality is `==` (Two equals signs!). 
# Remember: Single `=` assigns a value. Double `==` asks a question: "Are they equal?"
is_same_level = (boss_level == player_level)
print(f"Is player same level as boss? {is_same_level}")

# Inequality is `!=` (Not Equal)
print(f"Is boss stronger than player? {boss_level > player_level}")


print("\n--- SECTION 3: LOGICAL OPERATORS (AND, OR, NOT) ---")
# Advanced game mechanics and AI require multiple conditions at once!

has_key = True
door_is_unlocked = False

# 'or' requires ONLY ONE condition to be True.
can_enter_room = has_key or door_is_unlocked
print(f"Can the player enter the room? {can_enter_room}")

# 'and' requires BOTH conditions to be True.
mana_points = 50
spell_cost = 30
has_learned_spell = True

can_cast_spell = (mana_points >= spell_cost) and has_learned_spell
print(f"Can cast Fireball? {can_cast_spell}")

# 'not' flips a Boolean (True becomes False, False becomes True)
is_poisoned = False
print(f"Is player safe from poison? {not is_poisoned}")


print("\n--- SECTION 4: TRUTHY AND FALSY (ADVANCED PROFESSIONAL TRICK) ---")
# In Python, almost EVERYTHING can be treated as True or False!
# Zero (0), empty strings (""), and empty lists ([]) are considered "Falsy".
# Everything else is "Truthy".
# Professionals use this to check if a string is empty or if a score is zero!

inventory = "" # Empty string (Falsy)

if inventory:
    print("You have items in your inventory.")
else:
    print("Your inventory is completely empty! (This string was Falsy)")


# ============================================================================
# 🛑 END OF MODULE 3 
# ============================================================================
# HOMEWORK / PRACTICE:
# 1. Create a variable `temperature` and set it to a number (e.g., 25).
# 2. Write an `if / elif / else` block:
#    - If temp is greater than 30, print "It's scorching hot!"
#    - If it's between 20 and 30 (inclusive), print "The weather is perfect."
#    - Else, print "It's getting cold."
#    (Hint for the middle one: `elif temperature >= 20 and temperature <= 30:`)
# 3. Create an empty string `player_input = ""` and use an `if / else` statement
#    to print "User typed something" or "User pressed Enter without typing".
#
# Test your code (python Python-Learning.py) and tell me when you're ready!
# ============================================================================
