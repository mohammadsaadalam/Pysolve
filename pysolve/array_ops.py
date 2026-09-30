"""Module 2: Array / list techniques (Syllabus Unit 5).

Functions never modify the caller's list; they work on copies.
"""


def reverse_array(arr):
    """Reverse the order of an array using two pointers."""
    result = arr[:]
    left = 0
    right = len(result) - 1
    while left < right:
        result[left], result[right] = result[right], result[left]
        left = left + 1
        right = right - 1
    return result


def count_occurrences(arr, target):
    """Count how many times `target` appears in the array."""
    count = 0
    for item in arr:
        if item == target:
            count = count + 1
    return count


def frequency_table(arr):
    """Return a dictionary {value: count} for every value in the array."""
    table = {}
    for item in arr:
        if item in table:
            table[item] = table[item] + 1
        else:
            table[item] = 1
    return table


def find_max(arr):
    """Find the largest element."""
    if len(arr) == 0:
        raise ValueError("The array is empty.")
    largest = arr[0]
    for item in arr:
        if item > largest:
            largest = item
    return largest


def find_min(arr):
    """Find the smallest element."""
    if len(arr) == 0:
        raise ValueError("The array is empty.")
    smallest = arr[0]
    for item in arr:
        if item < smallest:
            smallest = item
    return smallest


def insertion_sort(arr):
    """Return a sorted copy of the array (insertion sort)."""
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j = j - 1
        result[j + 1] = key
    return result


def is_sorted(arr):
    """True if the array is in non-decreasing order."""
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


def remove_duplicates_sorted(arr):
    """Remove duplicates from an ORDERED array in a single pass."""
    if not is_sorted(arr):
        raise ValueError("The array must be sorted (ascending) first.")
    if len(arr) == 0:
        return []
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(arr[i])
    return result


def remove_duplicates_set(arr):
    """Remove duplicates using a set (keeps first-seen order).

    Time trade-off: O(n) time but uses extra memory for the set,
    compared with sorting first (O(n^2) with insertion sort).
    """
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def partition(arr, pivot):
    """Partition around a pivot value.

    Returns (smaller, equal, larger) as three lists.
    """
    smaller = []
    equal = []
    larger = []
    for item in arr:
        if item < pivot:
            smaller.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            larger.append(item)
    return smaller, equal, larger


def kth_smallest(arr, k):
    """Find the kth smallest element (k starts at 1) using quick-select."""
    if len(arr) == 0:
        raise ValueError("The array is empty.")
    if k < 1 or k > len(arr):
        raise ValueError("k must be between 1 and " + str(len(arr)) + ".")
    current = arr[:]
    while True:
        pivot = current[len(current) // 2]
        smaller, equal, larger = partition(current, pivot)
        if k <= len(smaller):
            current = smaller
        elif k <= len(smaller) + len(equal):
            return pivot
        else:
            k = k - len(smaller) - len(equal)
            current = larger
