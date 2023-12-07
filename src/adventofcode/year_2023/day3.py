from adventofcode import AdventOfCode
from math import prod
INPUT_DATA = "inputs/2023/day3.txt"

def check_string(input: str):
    edited_str = input.replace(".", "")
    return len(edited_str) > 0 and not edited_str[0].isdecimal()

class Day3(AdventOfCode):
    def __init__(self):
        super().__init__(input_path=INPUT_DATA)
        
    def resolve_part_1(self) -> int:
        sum = 0
        for line_index, line in enumerate(self.data):
            digit_found = 0
            digit_start_index = 0
            digit_end_index = 0
            for i, char in enumerate(line):
                if char.isdecimal():
                    if digit_found == 0:
                        digit_start_index = i
                    digit_found = 1
                    if i == len(line) - 1 or not line[i+1].isdecimal():
                        digit_found = 0
                        digit_end_index = i
                        digit = int(line[digit_start_index : digit_end_index + 1])
                        check_start = digit_start_index - 1 if digit_start_index - 1 >= 0 else digit_start_index
                        check_end = digit_end_index + 1 if digit_end_index + 1 < len(line) else digit_end_index
                        if line_index - 1 >= 0:
                            if check_string(self.data[line_index - 1][check_start : check_end + 1]):
                                sum += digit
                                continue
                        if check_string("".join([line[check_start], line[check_end]])):
                            sum += digit
                            continue
                        if line_index + 1 < len(self.data):
                            if check_string(self.data[line_index + 1][check_start : check_end + 1]):
                                sum += digit
                                continue
        return sum

    def resolve_part_2(self) -> int:
        just_dots = "." * len(self.data[0])
        edited_data = self.data
        edited_data.insert(0, just_dots)
        edited_data.append(just_dots)
        for i, _ in enumerate(edited_data):
            edited_data[i] = "..." + edited_data[i] + "..."
        
        sum = 0
        
        for line_index, line in enumerate(edited_data):
            if line_index not in range(1, len(line) - 1):
                continue
            for char_index, char in enumerate(line):
                if char == "*":
                    numbers: list[int] = []
                    y_offset = -1
                    while y_offset <= 1:
                        row = edited_data[line_index + y_offset][char_index - 3 : char_index + 4]
                        middle_symbol_index = len(row) // 2 # or just 3
                        middle_symbol = row[middle_symbol_index]
                        if row[middle_symbol_index - 1: middle_symbol_index + 2] != "...":
                            if middle_symbol.isdecimal():
                                numbers.append(max([int(s) for s in row.split(".") if s.isdigit()]))
                            else:
                                left_part = row[:middle_symbol_index]
                                right_part = row[middle_symbol_index + 1:]
                                if left_part[-1].isdecimal():
                                    numbers.append(max([int(s) for s in left_part.split(".") if s.isdigit()]))
                                if right_part[0].isdecimal():
                                    numbers.append(max([int(s) for s in right_part.split(".") if s.isdigit()]))
                        y_offset += 1
                    if len(numbers) == 2:
                        sum += prod(numbers)
        return sum