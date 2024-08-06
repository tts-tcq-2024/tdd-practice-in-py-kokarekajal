import re

def add(numbers):
    if not numbers:
        return 0
    delimiter, numbers = extract_delimiter(numbers)
    nums = parse_numbers(numbers, delimiter)
    validate_no_negatives(nums)
    return sum_ignoring_large_numbers(nums)

def extract_delimiter(numbers):
    if numbers.startswith("//"):
        parts = numbers.split("\n", 1)
        delimiter = re.escape(parts[0][2:])
        return delimiter, parts[1]
    return ",|\n", numbers

def parse_numbers(numbers, delimiter):
    return list(map(int, re.split(delimiter, numbers)))

def validate_no_negatives(nums):
    negatives = [num for num in nums if num < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {','.join(map(str, negatives))}")

def sum_ignoring_large_numbers(nums):
    return sum(num for num in nums if num <= 1000)
