from adventofcode import AdventOfCode

INPUT_DATA = "inputs/2023/day1.txt"

digits_list = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def handle_string(input: str) -> int:
    edited_string = input
    first_matches = [100] * 10
    last_matches = [-1] * 10
    for digit, spelled_digit in enumerate(digits_list):
        edited_string = edited_string.replace(str(digit), spelled_digit)
    for i in range(1, 10):
        f_match = edited_string.find(digits_list[i])
        first_matches[i] = f_match if f_match != -1 else 100
        last_matches[i] = edited_string.rfind(digits_list[i])
    return int(
        f"{first_matches.index(min(first_matches))}{last_matches.index(max(last_matches))}"
    )


class Day1(AdventOfCode):
    def __init__(self):
        super().__init__(input_path=INPUT_DATA)

    def resolve_part_1(self) -> int:
        sum = 0
        for line in self.data:
            filtred_str = "".join(filter(str.isdigit, line))
            if filtred_str:
                sum += int(filtred_str[0] + filtred_str[-1])
        return sum

    def resolve_part_2(self) -> int:
        sum = 0
        for line in self.data:
            sum += handle_string(line)
        return sum
