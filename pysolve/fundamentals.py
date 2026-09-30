"""Module 1: Fundamental algorithms (Syllabus Unit 3).

Every algorithm is written with basic loops and conditionals on purpose,
without using shortcuts like bin(), reversed() or math.factorial(),
so the logic of the algorithm itself is visible.
"""

DIGITS = "0123456789ABCDEF"


def swap_with_temp(a, b):
    """Exchange two values using a temporary variable."""
    temp = a
    a = b
    b = temp
    return a, b


def swap_without_temp(a, b):
    """Exchange two numbers using arithmetic (no temporary variable)."""
    a = a + b
    b = a - b
    a = a - b
    return a, b


def swap_tuple(a, b):
    """Exchange two values using Python's tuple assignment."""
    a, b = b, a
    return a, b


def sum_natural(n):
    """Summation of the first n natural numbers: 1 + 2 + ... + n."""
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total


def count_digits(n):
    """Counting: number of digits in an integer."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count


def sum_of_digits(n):
    """Summation of the digits of an integer."""
    n = abs(n)
    total = 0
    while n > 0:
        total = total + n % 10
        n = n // 10
    return total


def factorial(n):
    """Factorial of n (iterative). Raises ValueError for negative n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def fibonacci_nth(n):
    """Return the nth Fibonacci number (F0 = 0, F1 = 1)."""
    if n < 0:
        raise ValueError("Position must be 0 or greater.")
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_series(count):
    """Return a list containing the first `count` Fibonacci numbers."""
    if count < 0:
        raise ValueError("Count must be 0 or greater.")
    series = []
    a = 0
    b = 1
    for _ in range(count):
        series.append(a)
        a, b = b, a + b
    return series


def reverse_number(n):
    """Reverse the digits of an integer (keeps the sign)."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n = n // 10
    return sign * reversed_n


def is_palindrome_number(n):
    """True if the number reads the same forwards and backwards."""
    return n >= 0 and n == reverse_number(n)


def decimal_to_base(n, base):
    """Convert a non-negative decimal integer to the given base (2-16)."""
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16.")
    if n < 0:
        raise ValueError("Only non-negative numbers are supported.")
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        remainder = n % base
        result = DIGITS[remainder] + result
        n = n // base
    return result


def base_to_decimal(text, base):
    """Convert a string in the given base (2-16) to a decimal integer."""
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16.")
    text = text.strip().upper()
    if text == "":
        raise ValueError("Please enter a number to convert.")
    value = 0
    for ch in text:
        position = DIGITS.find(ch)
        if position == -1 or position >= base:
            raise ValueError("'" + ch + "' is not a valid digit in base " + str(base) + ".")
        value = value * base + position
    return value


def char_to_number(ch):
    """Character to number conversion (ASCII / Unicode code)."""
    if len(ch) != 1:
        raise ValueError("Please enter exactly one character.")
    return ord(ch)


def number_to_char(code):
    """Number to character conversion."""
    if code < 0 or code > 0x10FFFF:
        raise ValueError("Code is out of range.")
    return chr(code)


def text_to_numbers(text):
    """Convert every character in a string to its numeric code."""
    codes = []
    for ch in text:
        codes.append(ord(ch))
    return codes


def digit_string_to_number(text):
    """Convert a string like '4096' to the integer 4096 without int()."""
    text = text.strip()
    if text == "":
        raise ValueError("Please enter a number.")
    negative = text[0] == "-"
    if negative:
        text = text[1:]
    if text == "":
        raise ValueError("Please enter digits after the minus sign.")
    value = 0
    for ch in text:
        if ch < "0" or ch > "9":
            raise ValueError("'" + ch + "' is not a digit.")
        value = value * 10 + (ord(ch) - ord("0"))
    return -value if negative else value
