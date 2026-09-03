import numpy as np


# ============================================
# NumPy Boolean Masking Practice
# ============================================


# --------------------------------------------
# TASK 1: Create a NumPy array
# --------------------------------------------

die = np.array([1, 2, 3, 4, 5, 6])

print("Die:")
print(die)


# --------------------------------------------
# Find numbers greater than 2
# --------------------------------------------

print("\nNumbers greater than 2:")

for number in die:
    if number > 2:
        print(f"Number = {number}")


# --------------------------------------------
# Find even numbers
# --------------------------------------------

print("\nEven numbers:")

for number in die:
    if number % 2 == 0:
        print(f"Number = {number}")


# --------------------------------------------
# Boolean Masking
# --------------------------------------------

greater_than_2 = die > 2
even_numbers = die % 2 == 0

print("\nBoolean mask - greater than 2:")
print(greater_than_2)

print("\nBoolean mask - even numbers:")
print(even_numbers)


# --------------------------------------------
# Logical OR
# --------------------------------------------

print("\nOR condition:")
print(greater_than_2 | even_numbers)


# --------------------------------------------
# Logical AND
# --------------------------------------------

print("\nAND condition:")
print(greater_than_2 & even_numbers)


# --------------------------------------------
# TASK 2: Find even numbers
# --------------------------------------------

print("\nTASK 2 - Even numbers:")

for number in die:
    if number % 2 == 0:
        print(f"Number = {number}")


# --------------------------------------------
# Find numbers greater than 4
# --------------------------------------------

print("\nTASK 2 - Numbers greater than 4:")

for number in die:
    if number > 4:
        print(f"Number = {number}")