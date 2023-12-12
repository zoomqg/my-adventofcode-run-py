import numpy as np
from adventofcode import AdventOfCode
from typing import Iterable

INPUT_DATA = "inputs/2023/day4.txt"

def convert_input(input: list[str]):
    playing_numbers = []
    winning_numbers = []
    for line in input:
        card_numbers = line.split(":")[1].split("|")
        winning_numbers.append([int(x) for x in card_numbers[0].split(" ") if x])
        playing_numbers.append([int(x) for x in card_numbers[1].split(" ") if x])
    return winning_numbers, playing_numbers
        
class Day4(AdventOfCode):
    def __init__(self):
        super().__init__(input_path=INPUT_DATA)
        
    def resolve_part_1(self) -> int:
        winning_numbers, playing_numbers = convert_input(self.data)
        point_sum = 0
        for i, card in enumerate(playing_numbers):
            matches = sum(np.isin(card, winning_numbers[i]))
            if matches > 0:
                point_sum += 2 ** (matches - 1) 
        return point_sum
    
    def resolve_part_2(self) -> int:
        winning_numbers, playing_numbers = convert_input(self.data)
        instances = [1] * len(winning_numbers)
        for i, card in enumerate(playing_numbers):
            matches = sum(np.isin(card, winning_numbers[i]))
            if matches:
                for card_copy in range(i + 1, i + 1 + matches):
                    instances[card_copy] += 1 * instances[i]
        return(sum(instances))