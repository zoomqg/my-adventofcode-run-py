class AdventOfCode:
    def __init__(self, input_path):
        if input_path:
            file = open(input_path, "r")
            raw_data = file.read()
            self.data = raw_data.split("\n")

    def resolve_part_1(self) -> int:
        return None

    def resolve_part_2(self) -> int:
        return None
    
    def print_result(self):
        part_1_result = self.resolve_part_1()
        part_2_result = self.resolve_part_2()
        print(f"Answer for part 1: {part_1_result}")
        print(f"Answer for part 2: {part_2_result}")
