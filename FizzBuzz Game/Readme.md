🎮 FizzBuzz Game (Python)

A simple Python implementation of the classic FizzBuzz game — with a small twist.
This project contains two different implementations of the same logic, demonstrating different coding styles and approaches.

📜 Rules
For each number from 1 up to a user-defined limit:

✅ Divisible by 3 and 7 → "FizzBuzz"
✅ Divisible by 3 → "Fizz"
✅ Divisible by 7 → "Buzz"
✅ Contains the digit "3" → "Almost Fizz"
🔢 Otherwise → the number itself

🧩 Project Structure
fizzbuzz.py
README.md

The Python file includes:
Option 1 – Conditional chain version (if / elif / else)
Option 2 – Accumulation (string-building) version

🔹 Option 1 – Conditional Chain

Uses a structured if-elif-else approach.
Characteristics
Clear execution order
Early returns
Straightforward logic
Returns integers when no condition matches
Best for: learning conditionals and control flow.

🔹 Option 2 – Accumulation Method

Builds the result dynamically using string concatenation.
Characteristics
More scalable
Cleaner when adding new rules
Always returns a string
Avoids long conditional chains
Best for: extensibility and cleaner rule expansion.

🖥 Example

Input:
15

Output:
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
                                      
🧠 Concepts Covered
Functions
Loops (for)
Conditionals (if, elif, else)
Modulo operator (%)
String manipulation
User input handling

📚 Purpose
This project serves as a learning exercise to demonstrate:
Basic Python control flow
Two different approaches to solving the same problem
Clean and readable coding structure

📄 License
Open-source and free to use for educational purposes.
