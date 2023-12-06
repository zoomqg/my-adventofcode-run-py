from adventofcode import AdventOfCode
from math import prod
INPUT_DATA = "inputs/2023/day2.txt"
COLOR_LIMITS = {
    "red": 12,
    "green": 13,
    "blue": 14
}

COLOR_INDEXES = {
    "red": 0,
    "green": 1,
    "blue": 2
}

class Day2(AdventOfCode):
    def __init__(self):
        super().__init__(input_path=INPUT_DATA)
        self.processed_inventories: list[str] = []
        for line in self.data:
            self.processed_inventories.append(line.split(":")[1].replace(";", ","))
            
    def resolve_part_1(self) -> int:
        sum_of_cool_games = 0
        for game_id, inventory in enumerate(self.processed_inventories):
            limit_reached = 0
            for item in inventory.split(","):
                splited_item = item.split(" ") # item.split should look like that: ["", "1", "green"]
                if int(splited_item[1]) > COLOR_LIMITS[splited_item[2]]:
                    limit_reached = 1
            if limit_reached == 0:
                sum_of_cool_games += game_id + 1 # +1 since first game has id 1
        return sum_of_cool_games

    
    def resolve_part_2(self) -> int:
        power_sum = 0
        for inventory in self.processed_inventories:
            highest_cubes = [0,0,0]
            for item in inventory.split(","):
                splited_item = item.split(" ") # item.split should look like that: ["", "1", "green"]
                amount_of_cubes = int(splited_item[1])
                item_title = splited_item[2]
                if amount_of_cubes > highest_cubes[COLOR_INDEXES[item_title]]:
                    highest_cubes[COLOR_INDEXES[item_title]] = amount_of_cubes
            power_sum += prod(highest_cubes)
        return power_sum