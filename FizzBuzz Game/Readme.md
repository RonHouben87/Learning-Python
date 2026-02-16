# FizzBuzz Game (Python)

## Project Description

The **FizzBuzz Game** is a Python implementation of the classic FizzBuzz problem, extended with an additional rule.

The program generates output for numbers from 1 up to a user-defined limit, applying a set of logical conditions to determine what should be printed for each number.

This project demonstrates two different implementations of the same logic, allowing comparison between coding styles and approaches.

---

## Game Rules

For each number from 1 up to the chosen limit:

- If the number is divisible by **3 and 7** → print `"FizzBuzz"`
- If the number is divisible by **3** → print `"Fizz"`
- If the number is divisible by **7** → print `"Buzz"`
- If the number contains the digit `"3"` → print `"Almost Fizz"`
- Otherwise → print the number itself

---

## Project Structure

```
fizzbuzz.py
README.md
```

The Python file contains two separate implementations of the same game logic.

---

## Program Structure

The program is divided into:

- User input handling  
- A loop from 1 to the chosen limit  
- Conditional logic for rule evaluation  
- Two different implementation styles  

Both versions produce the same output but use different internal logic.

---

## Implementation Approaches

### Option 1 – Conditional Chain

This version uses a structured `if / elif / else` chain.

Example structure:

```python
if condition_1:
    ...
elif condition_2:
    ...
elif condition_3:
    ...
else:
    ...
```

### Characteristics

- Clear execution order
- Easy to read for beginners
- Stops checking once a condition matches
- Returns integers when no rule applies

### Best For

- Learning conditional statements
- Understanding control flow
- Writing straightforward decision logic

---

### Option 2 – Accumulation Method

This version builds the output dynamically using string concatenation.

Instead of stopping at the first match, it:

- Creates an empty string
- Adds parts ("Fizz", "Buzz") when conditions match
- Prints the number if no string was built

Example concept:

```python
result = ""

if divisible_by_3:
    result += "Fizz"

if divisible_by_7:
    result += "Buzz"

if result == "":
    result = str(number)
```

### Characteristics

- More scalable
- Cleaner when adding new rules
- Avoids long conditional chains
- Always returns a string

### Best For

- Expanding rule sets
- Writing flexible logic
- Improving code scalability

---

## Example

### Input

```
15
```

### Output

```
1
2
Fizz
4
5
Fizz
Buzz
8
Fizz
10
11
Fizz
Almost Fizz
13
Fizz
FizzBuzz
```

---

## Concepts Demonstrated

This project covers several core Python concepts:

- Functions  
- `for` loops  
- Conditional statements (`if`, `elif`, `else`)  
- Modulo operator (`%`)  
- String manipulation  
- Type conversion  
- User input handling  

---

## Logical Flow of the Program

1. Ask the user for a number limit.
2. Loop from 1 up to that number.
3. Apply the game rules in order.
4. Print the appropriate output.
5. Repeat until the loop finishes.

Both implementations follow this same logical flow but differ internally in how conditions are evaluated.

---

## Purpose of the Project

This project is designed as a learning exercise to:

- Practice Python control flow
- Compare two different problem-solving approaches
- Improve understanding of conditional logic
- Write clean and readable code
- Explore scalability in simple programs

---

## Conclusion

The FizzBuzz Game demonstrates how the same problem can be solved in multiple ways.  

By comparing a traditional conditional chain with a more flexible accumulation method, this project highlights differences in readability, scalability, and design choices in Python programming.
