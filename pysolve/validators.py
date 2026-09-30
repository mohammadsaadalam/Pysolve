"""Input validation helpers. All raise ValueError with a friendly message."""


def parse_int(text, name="Value"):
    """Convert text to an integer or raise ValueError."""
    text = text.strip()
    if text == "":
        raise ValueError(name + " cannot be empty.")
    try:
        return int(text)
    except ValueError:
        raise ValueError(name + " must be a whole number (got '" + text + "').")


def parse_non_negative(text, name="Value"):
    """Convert text to an integer >= 0."""
    number = parse_int(text, name)
    if number < 0:
        raise ValueError(name + " must be 0 or greater.")
    return number


def parse_int_list(text):
    """Convert '4 8 15 16' or '4,8,15,16' into [4, 8, 15, 16]."""
    text = text.replace(",", " ").strip()
    if text == "":
        raise ValueError("Please enter at least one number.")
    numbers = []
    for part in text.split():
        numbers.append(parse_int(part, "Element"))
    return numbers


def parse_choice(text, low, high):
    """Validate a menu choice between low and high (inclusive)."""
    choice = parse_int(text, "Choice")
    if choice < low or choice > high:
        raise ValueError("Choice must be between " + str(low) + " and " + str(high) + ".")
    return choice
