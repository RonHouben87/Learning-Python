# Daily Expense Tracker

## Project Description

The **Daily Expense Tracker** is a command-line Python application that allows users to record and manage daily expenses.

The program provides an interactive menu where users can:

1. Add a new expense  
2. View all recorded expenses  
3. Calculate the total and average expense  
4. Clear all expenses  
5. Exit the program  

This project demonstrates fundamental Python concepts such as loops, conditionals, lists, and basic calculations.

---

## Program Structure

The program is organized into the following logical sections:

- Welcome message and menu display  
- Data initialization  
- Main program loop  
- Menu option handling  
- Input validation  

---

## Welcome Message and Menu

At startup, the program prints a welcome message and displays the menu options:

```text
Welcome to the Daily Expense Tracker!

Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit
```

---

## Data Storage

The program uses a list to store expense amounts:

```python
expenses = []
```

- Each expense is stored as a `float`
- The list dynamically grows when new expenses are added
- All calculations are based on this list

Note: Data is stored in memory and will be lost when the program exits.

---

## Main Loop

The program runs inside an infinite loop:

```python
while True:
```

This keeps the application running until the user selects option 5 (Exit).

---

## Menu Options Explained

### 1. Add a New Expense

- The user enters a numeric amount.
- The value is converted to a `float`.
- The amount is added to the list using:

```python
expenses.append(amount)
```

---

### 2. View All Expenses

- The program checks if the list is empty using:

```python
len(expenses) == 0
```

- If empty, a message is shown.
- Otherwise, all expenses are displayed with numbering.

Example output:

```text
Your expenses:
1. 15.0
2. 8.5
3. 22.75
```

---

### 3. Calculate Total and Average

If expenses exist:

- A loop calculates the total.
- The average is calculated using:

```python
average = total / len(expenses)
```

Both values are printed.

---

### 4. Clear All Expenses

The list is cleared using:

```python
expenses.clear()
```

This removes all stored expenses while keeping the same list object.

---

### 5. Exit

The program exits the loop using:

```python
break
```

A goodbye message is printed before termination.

---

## Invalid Input Handling

If the user enters a number outside the range 1–5, the program executes:

```python
print("Invalid choice. Please try again.")
```

This ensures the program continues running without crashing.

---

## Python Concepts Used

- `while` loops  
- `if / elif / else` statements  
- Lists  
- `append()` and `clear()` methods  
- `len()` function  
- `for` loops  
- Type conversion (`float()`)  
- Basic arithmetic operations  

---

## Limitations

- No validation for non-numeric expense input  
- No persistent data storage  
- No categories or dates  
- No currency formatting  

---

## Conclusion

This project is a beginner-friendly example of how to build an interactive console application in Python using core programming concepts.
