import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiters = [',', '\n']

    # Check for custom delimiter
    if numbers.startswith('//'):
        parts = numbers.split('\n', 1)
        delimiter_part = parts[0][2:]
        delimiter_part, numbers = numbers.split('\n', 1)
        delimiter_part = delimiter_part[2:]

        # Handle case with multiple delimiters enclosed in []
        if delimiter_part.startswith('[') and delimiter_part.endswith(']'):
            delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
        else:
            delimiters = [delimiter_part]

        numbers = parts[1]
        delimiters = re.findall(r'\[(.*?)\]', delimiter_part) or [delimiter_part]

    delimiters_regex = '|'.join(map(re.escape, delimiters))

    num_list = re.split(delimiters_regex, numbers)

    total_sum = 0
    negatives = []

    for num in num_list:
        if num:
            try:
                n = int(num)
            except ValueError:
                raise ValueError(f"Invalid number found: {num}")

            n = int(num)
            if n < 0:
                negatives.append(n)
            elif n <= 1000:
