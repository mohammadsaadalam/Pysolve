# PySolve — Fundamental Algorithms & Array Toolkit

A menu-driven Python toolkit for **CSE1021 – Introduction to Problem Solving and Programming**. PySolve lets first-year students run fundamental algorithms and array/list techniques from the command line, with input validation, error handling, run history, usage statistics, logging, and automated tests.

## Overview

PySolve is organized into three major functional modules:

1. **Fundamental Algorithms** — number manipulation, summation, factorial, Fibonacci, reversal, palindrome checking, base conversion, and character/code-point conversion.
2. **Array / List Techniques** — reversal, counting, frequency tables, max/min, insertion sort, duplicate removal, partitioning, and Kth-smallest selection.
3. **CLI, History & Statistics** — menu-driven interaction, validation, operation history, usage statistics, and logging.

The algorithms are intentionally implemented with basic Python constructs so that the underlying logic is visible rather than hidden behind shortcuts such as `bin()`, `reversed()`, or `math.factorial()`.

## Features

### Module 1 — Fundamental Algorithms
- Exchange two values using:
  - temporary variable
  - arithmetic
  - tuple assignment
- Sum the first *n* natural numbers
- Count digits and calculate digit sums
- Factorial
- Fibonacci series and nth Fibonacci number
- Reverse a number and check for palindromes
- Decimal → any base from 2–16
- Any base from 2–16 → decimal
- Text → Unicode code points
- Unicode code point → character
- Digit string → integer without using `int()`

### Module 2 — Array / List Techniques
- Reverse an array using two pointers
- Count occurrences
- Build a frequency table using a dictionary
- Find maximum and minimum
- Insertion sort
- Remove duplicates using:
  - sorted-array processing
  - a set
- Partition values around a pivot
- Find the Kth smallest element using quick-select

### Module 3 — CLI, History & Statistics
- Numbered menu navigation with Back/Exit options
- Centralized input validation
- Run history stored as a list of dictionaries
- Operation-frequency statistics
- Most-used operation
- Tried vs. not-tried operation tracking using sets
- Error and activity logging

## Technologies Used

- **Python 3.8+**
- Python standard library only
- `unittest` for automated testing
- `logging` for application logs
- `datetime` for operation timestamps
- Git / GitHub for version control
- Mermaid diagrams for project documentation

## Project Structure

```text
pysolve/
├── main.py
├── pysolve/
│   ├── __init__.py
│   ├── fundamentals.py
│   ├── array_ops.py
│   ├── menu.py
│   ├── history.py
│   ├── validators.py
│   └── logger.py
├── tests/
│   ├── test_fundamentals.py
│   ├── test_array_ops.py
│   ├── test_history.py
│   └── test_validators.py
├── docs/
│   └── design.md
├── statement.md
├── README.md
└── .gitignore
```

## Installation & Run

Clone the repository:

```bash
git clone <https://github.com/mohammadsaadalam/Pysolve.git>
cd pysolve
```

Run the application:

```bash
python main.py
```

No third-party packages are required.

## Testing

Run the complete test suite:

```bash
python -m unittest discover -s tests -t . -v
```

The current test suite contains **21 automated tests** covering normal cases, boundary cases, invalid inputs, round-trip base conversion, and list-mutation behavior.

## Example

```text
========================================================
  PySolve - Fundamental Algorithms & Array Toolkit
========================================================

 MAIN MENU
  1. Fundamental Algorithms
  2. Array / List Techniques
  3. History & Statistics
  0. Exit
```

Example operation:

```text
Your choice: 1

Fundamental Algorithms
1. Exchange two values
...
8. Decimal -> Binary/Octal/Hex (any base 2-16)
...
Your choice: 8
Decimal number: 255
Target base (2-16): 16
Result: FF
```

## Time Complexity Summary

| Operation | Typical complexity |
|---|---:|
| Sum / factorial / Fibonacci series | O(n) |
| Fibonacci nth term | O(n) |
| Base conversion | O(log n) for decimal input |
| Max / Min / Count / Reverse | O(n) |
| Insertion sort | O(n²) |
| Remove duplicates using set | O(n) average |
| Remove duplicates after insertion sort | O(n²) with the implemented sort |
| Partition | O(n) |
| Kth smallest (quick-select) | O(n) average, O(n²) worst case |

## Documentation

- [`statement.md`](statement.md) — problem statement, scope, target users, and high-level features
- [`docs/design.md`](docs/design.md) — objectives, functional/non-functional requirements, architecture, workflow, UML diagrams, design decisions, and testing approach

## Academic Context

This project was developed as a **VITyarthi Build Your Own Project** for CSE1021. It is intended to demonstrate practical application of introductory programming concepts through a modular, tested Python application.
