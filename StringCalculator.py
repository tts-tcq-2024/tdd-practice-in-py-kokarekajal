import re
class StringCalculator:
    
    def add(numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiters, numbers = StringCalculator.extract_delimiters(numbers)
        num_list = StringCalculator.split_numbers(numbers, delimiters)
        total_sum, negatives = StringCalculator.calculate_sum_and_check_negatives(num_list)
        
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
        
        return total_sum

  
    def extract_delimiters(numbers: str):
        delimiters = [',', '\n']
        if numbers.startswith('//'):
            delimiter_part, numbers = numbers[2:].split('\n', 1)
            delimiters = re.findall(r'\[(.*?)\]', delimiter_part) or [delimiter_part]
        return delimiters, numbers

  
    def split_numbers(numbers: str, delimiters: list):
        delimiters_regex = '|'.join(map(re.escape, delimiters))
        return re.split(delimiters_regex, numbers)

   
    def calculate_sum_and_check_negatives(num_list: list):
        total_sum = 0
        negatives = []
        for num in num_list:
            if num:
                n = int(num)
                if n < 0:
                    negatives.append(n)
                elif n <= 1000:
                    total_sum += n
        return total_sum, negatives
