import re
def Add(numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiters = [',', '\n']
        custom_delimiter = False
        
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            delimiter_part = parts[0][2:]
            
            if delimiter_part.startswith('[') and delimiter_part.endswith(']'):
                delimiters = re.findall(r'\[(.*?)\]', delimiter_part)
            else:
                delimiters = [delimiter_part]
            
            numbers = parts[1]
            custom_delimiter = True
        
        delimiters_regex = '|'.join(map(re.escape, delimiters))
        num_list = re.split(delimiters_regex, numbers)
        
        sum = 0
        negatives = []
        
        for num in num_list:
            if num:
                try:
                    n = int(num)
                except ValueError:
                    raise ValueError(f"Invalid number found: {num}")
                
                if n < 0:
                    negatives.append(n)
                elif n <= 1000:
                    sum += n
        
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
        
        return sum



