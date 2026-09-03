# NumPy Boolean Masking Practice

A beginner-friendly NumPy practice project focused on arrays, conditional filtering, loops, modulo operations, Boolean masking, and logical operators.

## 📚 Topics Covered

* Creating NumPy arrays
* Iterating through arrays using `for` loops
* Using `if` conditions
* Comparison operators
* Modulo `%` operator
* Finding even numbers
* Filtering values
* Boolean masking
* Boolean indexing
* Logical OR `|`
* Logical AND `&`

## 🛠️ Technologies

* Python 3
* NumPy

## 📌 Project Overview

This project contains simple exercises for practicing NumPy arrays and conditions.

The main array used in the exercises is:

```python
die = np.array([1, 2, 3, 4, 5, 6])
```

The project demonstrates how to:

1. Create a NumPy array.
2. Loop through array elements.
3. Find numbers greater than a specific value.
4. Find even numbers.
5. Create Boolean masks.
6. Combine Boolean conditions using `|` and `&`.

## 🔹 Boolean Masking

Boolean masking allows us to create a Boolean array based on a condition.

Example:

```python
greater_than_2 = die > 2
```

The result is:

```text
[False False  True  True  True  True]
```

Another example:

```python
even_numbers = die % 2 == 0
```

The result is:

```text
[False  True False  True False  True]
```

## 🔹 Logical OR

The `|` operator combines two Boolean conditions.

```python
greater_than_2 | even_numbers
```

This returns `True` when at least one of the two conditions is `True`.

## 🔹 Logical AND

The `&` operator combines two Boolean conditions.

```python
greater_than_2 & even_numbers
```

This returns `True` only when both conditions are `True`.

## 📌 Practice Tasks

### Task 1

* Create a NumPy array containing numbers from 1 to 6.
* Find numbers greater than 2.
* Find even numbers.
* Create Boolean masks.
* Combine conditions using OR and AND.

### Task 2

* Find even numbers.
* Find numbers greater than 4.

## 💻 Example

```python
import numpy as np

die = np.array([1, 2, 3, 4, 5, 6])

greater_than_2 = die > 2
even_numbers = die % 2 == 0

print(greater_than_2)
print(even_numbers)

print(greater_than_2 | even_numbers)
print(greater_than_2 & even_numbers)
```

## 📖 What I Learned

Through this project, I practiced:

* Working with NumPy arrays.
* Using loops with arrays.
* Applying conditions to data.
* Using the modulo operator to identify even numbers.
* Creating Boolean masks.
* Combining multiple Boolean conditions.
* Understanding the difference between normal Python conditions and NumPy Boolean operations.

## 🚀 Installation

Install NumPy using:

```bash
pip install numpy
```

Or install all project dependencies using:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run

Run the Python file:

```bash
python numpy_boolean_masking.py
```

## 📂 Project Structure

```text
numpy-boolean-masking-practice/
│
├── numpy_boolean_masking.py
├── requirements.txt
└── README.md
```

## 🎯 Purpose

This project is part of my Python and NumPy learning journey.

It is designed to strengthen fundamental NumPy skills that are useful for Data Science and Machine Learning.

## 📄 License

This project is for educational and practice purposes.
