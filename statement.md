# Project Statement — PySolve

## Problem Statement
Beginners in programming often understand an algorithm on paper but struggle to see it
working on real inputs, compare different ways of solving the same problem, or check
their own answers. There is no single, simple, safe place to try the core algorithms of an
introductory programming course and see the results with clear error messages.

**PySolve** is a menu-driven Python toolkit that implements the fundamental algorithms and
array techniques of the course from first principles (without built-in shortcuts), validates
every input, and keeps a history of what the user has tried.

## Scope
**In scope**
- Fundamental algorithms: exchange of values, counting, summation, factorial, Fibonacci,
  number reversal, base conversion, character-to-number conversion.
- Array techniques: reversal, counting, max/min, duplicate removal, partitioning, Kth smallest.
- Compound data usage: history stored as a list of dictionaries, with tuples and sets used
  for statistics.
- Input validation, error handling, logging and unit tests.

**Out of scope**
- Graphical interface, databases, web/network features, file-based storage of records.

## Target Users
- First-year students learning problem solving and Python.
- Instructors who want a quick demo of basic algorithms and their edge cases.

## High-Level Features
1. **Fundamental Algorithms Engine** — 12 operations covering Unit 3 algorithms.
2. **Array / List Processing Engine** — 6 operations covering Unit 5 techniques.
3. **Interactive CLI with History & Statistics** — validated menus, run history,
   usage counts and "operations tried vs not tried" using set operations.
