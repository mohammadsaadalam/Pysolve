"""Module 3b: Run history using lists, dictionaries, tuples and sets (Unit 5)."""

from datetime import datetime

# Compound data: a list of dictionaries, one per operation performed.
_history = []


def add_record(category, operation, user_input, output):
    """Store one operation and return the record."""
    record = {
        "id": len(_history) + 1,
        "category": category,
        "operation": operation,
        "input": str(user_input),
        "output": str(output),
        "time": datetime.now().strftime("%H:%M:%S"),
    }
    _history.append(record)
    return record


def get_history():
    """Return a copy of all records."""
    return _history[:]


def clear_history():
    """Delete all records."""
    _history.clear()


def count_by_operation():
    """Dictionary {operation: number of times used}."""
    counts = {}
    for record in _history:
        name = record["operation"]
        counts[name] = counts.get(name, 0) + 1
    return counts


def unique_operations():
    """Set of distinct operations the user has tried."""
    names = set()
    for record in _history:
        names.add(record["operation"])
    return names


def most_used_operation():
    """Return (operation, count) for the most used operation, or None."""
    counts = count_by_operation()
    best = None
    for name in counts:
        if best is None or counts[name] > best[1]:
            best = (name, counts[name])
    return best


def coverage(all_operations):
    """Set operations: which operations tried vs. not yet tried.

    Returns a tuple (tried, not_tried).
    """
    tried = unique_operations()
    all_set = set(all_operations)
    return tried & all_set, all_set - tried
