import re

class StringCalculator:
    
    @staticmethod
    def add(numbers: str) -> int:
        if numbers == "":
            return 0

        delimiters, numbers = StringCalculator.extract_delimiters(numbers)
        num_list = StringCalculator.split_numbers(numbers, delimiters)
        total_sum = StringCalculator.sum_numbers(num_list)
        
        return total_sum

    @staticmethod
    def extract_delimiters(numbers: str):
        if not numbers.startswith('//'):
            return [',', '\n'], numbers
        
        delimiter_part, numbers = numbers[2:].split('\n', 1)
        delimiters = re.findall(r'\[(.*?)\]', delimiter_part) or [delimiter_part]
        return delimiters, numbers

    @staticmethod
    def split_numbers(numbers: str, delimiters: list):
        delimiters_regex = '|'.join(map(re.escape, delimiters))
        return re.split(delimiters_regex, numbers)

    @staticmethod
    def sum_numbers(num_list: list):
        total_sum = 0
        negatives = StringCalculator.find_negatives(num_list)
        StringCalculator.raise_if_negatives(negatives)
        for num in num_list:
            if num:
                n = int(num)
                if n <= 1000:
                    total_sum += n
        return total_sum

    @staticmethod
    def find_negatives(num_list: list):
        return [int(num) for num in num_list if num and int(num) < 0]

    @staticmethod
    def raise_if_negatives(negatives: list):
        if negatives:
            raise ValueError(f"negatives not allowed: {', '.join(map(str, negatives))}")
