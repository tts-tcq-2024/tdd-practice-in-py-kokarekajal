import re

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiters = [',', '\n']
    if numbers.startswith('//'):
        delimiter_part, numbers = numbers[2:].split('\n', 1)
        delimiters = re.findall(r'\[(.*?)\]', delimiter_part) or [delimiter_part]
    
    delimiters_regex = '|'.join(map(re.escape, delimiters))
    num_list = re.split(delimiters_regex, numbers)
    
    total_sum, negatives = 0, []
    for num in num_list:
        if num:
            n = int(num)
            if n < 0:
                negatives.append(n)
            elif n <= 1000:
                total_sum += n
    
    if negatives:
        raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
    
    return total_sum
