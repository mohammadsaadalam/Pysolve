"""Module 3a: Interactive menu-driven command line interface.

Flow: main menu -> category menu -> operation -> validated input -> result.
Each operation is a small function; a dictionary maps menu choices to them
(the "dispatcher").
"""

from pysolve import fundamentals as fd
from pysolve import array_ops as ao
from pysolve import validators as vl
from pysolve import history as hist
from pysolve.logger import log_info, log_error

LINE = "=" * 56


# ---------------------------------------------------------------- helpers
def ask(prompt):
    return input(prompt)


def show_result(category, operation, user_input, output):
    """Print a result and store it in the history."""
    print("  Result:", output)
    hist.add_record(category, operation, user_input, output)
    log_info(operation + " | input=" + str(user_input) + " | output=" + str(output))


# ------------------------------------------------- Module 1 operations
def op_swap():
    a = vl.parse_int(ask("  First number : "), "First number")
    b = vl.parse_int(ask("  Second number: "), "Second number")
    r1 = fd.swap_with_temp(a, b)
    r2 = fd.swap_without_temp(a, b)
    r3 = fd.swap_tuple(a, b)
    print("  With temp variable   :", r1)
    print("  Without temp variable:", r2)
    print("  Tuple assignment     :", r3)
    show_result("Fundamentals", "Exchange two values", (a, b), r1)


def op_sum():
    n = vl.parse_non_negative(ask("  Enter n: "), "n")
    show_result("Fundamentals", "Sum of first n natural numbers", n, fd.sum_natural(n))


def op_digits():
    n = vl.parse_int(ask("  Enter a number: "), "Number")
    print("  Digit count:", fd.count_digits(n))
    show_result("Fundamentals", "Count / sum digits of a number", n,
                "count=" + str(fd.count_digits(n)) + ", sum=" + str(fd.sum_of_digits(n)))


def op_factorial():
    n = vl.parse_non_negative(ask("  Enter n: "), "n")
    if n > 900:
        raise ValueError("n is too large for display; use 900 or less.")
    show_result("Fundamentals", "Factorial", n, fd.factorial(n))


def op_fibonacci():
    n = vl.parse_non_negative(ask("  How many terms? "), "Terms")
    if n > 1000:
        raise ValueError("Please use 1000 terms or fewer.")
    series = fd.fibonacci_series(n)
    print("  Series:", series)
    show_result("Fundamentals", "Fibonacci series", n, series)


def op_reverse_number():
    n = vl.parse_int(ask("  Enter a number: "), "Number")
    rev = fd.reverse_number(n)
    kind = "palindrome" if fd.is_palindrome_number(n) else "not a palindrome"
    show_result("Fundamentals", "Reverse a number (+ palindrome check)", n, str(rev) + " (" + kind + ")")


def op_dec_to_base():
    n = vl.parse_non_negative(ask("  Decimal number: "), "Number")
    base = vl.parse_int(ask("  Target base (2-16): "), "Base")
    show_result("Fundamentals", "Decimal -> Binary/Octal/Hex (any base 2-16)", (n, base), fd.decimal_to_base(n, base))


def op_base_to_dec():
    text = ask("  Number in source base: ")
    base = vl.parse_int(ask("  Source base (2-16): "), "Base")
    show_result("Fundamentals", "Any base -> Decimal", (text, base), fd.base_to_decimal(text, base))


def op_fibonacci_nth():
    n = vl.parse_non_negative(ask("  Position n (F0 = 0, F1 = 1): "), "Position")
    if n > 100000:
        raise ValueError("Position is too large; use 100000 or less.")
    show_result("Fundamentals", "Nth Fibonacci number", n, fd.fibonacci_nth(n))


def op_char_number():
    text = ask("  Enter text: ")
    if text == "":
        raise ValueError("Please enter some text.")
    show_result("Fundamentals", "Text -> Unicode code points", text, fd.text_to_numbers(text))


def op_number_char():
    code = vl.parse_non_negative(ask("  Enter Unicode code point: "), "Code")
    show_result("Fundamentals", "Number -> Character", code, fd.number_to_char(code))


def op_digit_string():
    text = ask("  Enter a digit string: ")
    show_result("Fundamentals", "Digit string -> Integer", text, fd.digit_string_to_number(text))


FUNDAMENTAL_MENU = {
    1: ("Exchange two values", op_swap),
    2: ("Sum of first n natural numbers", op_sum),
    3: ("Count / sum digits of a number", op_digits),
    4: ("Factorial", op_factorial),
    5: ("Fibonacci series", op_fibonacci),
    6: ("Nth Fibonacci number", op_fibonacci_nth),
    7: ("Reverse a number (+ palindrome check)", op_reverse_number),
    8: ("Decimal -> Binary/Octal/Hex (any base 2-16)", op_dec_to_base),
    9: ("Any base -> Decimal", op_base_to_dec),
    10: ("Text -> Unicode code points", op_char_number),
    11: ("Unicode code point -> Character", op_number_char),
    12: ("Digit string -> Integer (without int())", op_digit_string),
}


# ------------------------------------------------- Module 2 operations
def read_array():
    return vl.parse_int_list(ask("  Enter numbers (space/comma separated): "))


def op_reverse_array():
    arr = read_array()
    show_result("Arrays", "Reverse an array", arr, ao.reverse_array(arr))


def op_count():
    arr = read_array()
    target = vl.parse_int(ask("  Value to count: "), "Value")
    print("  Frequency table:", ao.frequency_table(arr))
    show_result("Arrays", "Count occurrences (+ frequency table)", (arr, target), ao.count_occurrences(arr, target))


def op_max_min():
    arr = read_array()
    show_result("Arrays", "Find maximum and minimum", arr,
                "max=" + str(ao.find_max(arr)) + ", min=" + str(ao.find_min(arr)))


def op_remove_dups():
    arr = read_array()
    ordered = ao.insertion_sort(arr)
    print("  Sorted array       :", ordered)
    print("  Using set (O(n))   :", ao.remove_duplicates_set(arr))
    show_result("Arrays", "Remove duplicates", arr, ao.remove_duplicates_sorted(ordered))


def op_partition():
    arr = read_array()
    pivot = vl.parse_int(ask("  Pivot value: "), "Pivot")
    smaller, equal, larger = ao.partition(arr, pivot)
    show_result("Arrays", "Partition around a pivot", (arr, pivot),
                "smaller=" + str(smaller) + " equal=" + str(equal) + " larger=" + str(larger))


def op_kth():
    arr = read_array()
    k = vl.parse_int(ask("  k (1 = smallest): "), "k")
    show_result("Arrays", "Find Kth smallest element", (arr, k), ao.kth_smallest(arr, k))


ARRAY_MENU = {
    1: ("Reverse an array", op_reverse_array),
    2: ("Count occurrences (+ frequency table)", op_count),
    3: ("Find maximum and minimum", op_max_min),
    4: ("Remove duplicates", op_remove_dups),
    5: ("Partition around a pivot", op_partition),
    6: ("Find Kth smallest element", op_kth),
}


# ------------------------------------------------- Module 3 operations
def show_history():
    records = hist.get_history()
    if len(records) == 0:
        print("  No operations performed yet.")
        return
    for r in records:
        print("  #" + str(r["id"]), r["time"], "|", r["operation"],
              "| in:", r["input"], "| out:", r["output"])


def show_statistics():
    records = hist.get_history()
    print("  Total operations:", len(records))
    if len(records) == 0:
        return
    for name, count in hist.count_by_operation().items():
        print("   -", name + ":", count)
    print("  Most used:", hist.most_used_operation())
    all_ops = []
    for menu in (FUNDAMENTAL_MENU, ARRAY_MENU):
        for title, _ in menu.values():
            all_ops.append(title)
    tried, not_tried = hist.coverage(all_ops)
    print("  Distinct operations tried:", len(tried), "of", len(all_ops))
    if len(not_tried) > 0:
        print("  Not tried yet:", sorted(not_tried))


HISTORY_MENU = {
    1: ("View history", show_history),
    2: ("View usage statistics", show_statistics),
    3: ("Clear history", lambda: (hist.clear_history(), print("  History cleared."))),
}


# ------------------------------------------------------------ menu loop
def run_submenu(title, menu):
    """Show a submenu and run the chosen operation until the user goes back."""
    while True:
        print("\n" + LINE)
        print(" " + title)
        print(LINE)
        for number in menu:
            print("  " + str(number) + ". " + menu[number][0])
        print("  0. Back")
        try:
            choice = vl.parse_choice(ask("\n  Your choice: "), 0, len(menu))
            if choice == 0:
                return
            menu[choice][1]()
        except ValueError as error:
            print("  [!] " + str(error))
            log_error(str(error))
        except (EOFError, KeyboardInterrupt):
            print("\n  Cancelled.")
            return


def main_menu():
    """Top-level loop of the application."""
    print(LINE)
    print("  PySolve - Fundamental Algorithms & Array Toolkit")
    print(LINE)
    log_info("Application started")
    sections = {
        1: ("Fundamental Algorithms", FUNDAMENTAL_MENU),
        2: ("Array / List Techniques", ARRAY_MENU),
        3: ("History & Statistics", HISTORY_MENU),
    }
    while True:
        print("\n MAIN MENU")
        for number in sections:
            print("  " + str(number) + ". " + sections[number][0])
        print("  0. Exit")
        try:
            choice = vl.parse_choice(ask("\n  Your choice: "), 0, len(sections))
        except ValueError as error:
            print("  [!] " + str(error))
            continue
        except (EOFError, KeyboardInterrupt):
            break
        if choice == 0:
            break
        run_submenu(sections[choice][0], sections[choice][1])
    print("\n  Goodbye!")
    log_info("Application closed")
