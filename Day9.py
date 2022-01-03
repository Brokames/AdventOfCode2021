from pprint import pprint
import datetime
import itertools as it


def main():
    begin_time = datetime.datetime.now()

    # Process input into mapped lines
    with open("C:\\Users\\Ja\\PycharmProjects\\AdventOfCode\\Day9Data.txt", "r") as fd:
        lines = fd.readlines()
    for i, line in enumerate(lines):
        lines[i] = str(line).rstrip()

    risk_total = 0
    low_coords = set()
    for i, line in enumerate(lines):
        for j, flow in enumerate(line):
            # Build conditional
            conditional = 1
            if i == 0:
                conditional = conditional and flow < lines[i + 1][j]
            elif i == len(lines) - 1:
                conditional = conditional and flow < lines[i - 1][j]
            else:
                conditional = conditional and flow < lines[i + 1][j] and flow < lines[i - 1][j]
            
            if j == 0:
                conditional = conditional and flow < line[j + 1]
            elif j == len(lines) - 1:
                conditional = conditional and flow < line[j - 1]
            else: 
                conditional = conditional and flow < line[j + 1] and flow < line[j - 1]

            # Evaluate
            if conditional: 
                risk_total += int(flow) + 1
                low_coords.add((i, j))

    low_coords = sorted(list(low_coords))
    walker = Walker((0, 0), lines)
    areas = []
    for coord in low_coords[:10]:
        walker.set_coords(coord)
        walker.set_direction("RIGHT")
        walker.get_basin_area()
    
    print(f"Total Risk: {risk_total}")

    print(datetime.datetime.now() - begin_time)

class Walker:
    def __init__(self, start_cords: tuple, heat_map: list) -> None:
        self.direction_atlas = {
            "RIGHT": 0,
            "UP"   : 1,
            "LEFT" : 2,
            "DOWN" : 3
        }
        self.curr_dir = self.direction_atlas["RIGHT"]
        if start_cords[0] < 0 or start_cords[1] < 0 or start_cords[0] > len(heat_map) - 1 or start_cords[1] > len(heat_map[0]):
            assert("Invalid starting coordinates for given heat map")
        else:
            self.curr_coords = start_cords
        self.heat_map = heat_map
    
    def get_direction(self) -> int:
        return self.curr_dir
    
    def set_direction(self, direction: str) -> None:
        try:
            self.curr_dir = self.direction_atlas[direction]
        except KeyError:
            assert("Invalid Direction")

    def get_coords(self) -> tuple:
        return self.curr_coords
    
    def set_coords(self, coords: tuple):
        self.curr_coords = coords
    
    def get_surroundings(self) -> list:
        output = [[], [], []]
        for i in range(9):
            try:
                if self.curr_coords[0] - 1 + i // 3 < 0 or self.curr_coords[1] - 1 + i % 3 < 0:
                    continue
                else:
                    output[i // 3].append(self.heat_map[self.curr_coords[0] - 1 + i // 3][self.curr_coords[1] - 1 + i % 3])
            except IndexError:
                pass
        return output
    
    def print_surroundings(self) -> None:
        for line in self.get_surroundings():
            [print(num, end = " ") for num in line if line]
            if line: print()
    
    def rotate_left(self) -> None:
        self.curr_dir = (self.curr_dir + 1) % 4
    
    def rotate_right(self) -> None:
        self.curr_dir = (self.curr_dir + 3) % 4
        
    def look_forward(self) -> int: 
        if self.direction_atlas["RIGHT"] == self.curr_dir and self.curr_coords[1] < len(self.heat_map[0]) - 1:
            return self.heat_map[self.curr_coords[0]][self.curr_coords[1] + 1]
        elif self.direction_atlas["UP"] == self.curr_dir and self.curr_coords[0] > 0:
            return self.heat_map[self.curr_coords[0] - 1][self.curr_coords[1]]
        elif self.direction_atlas["LEFT"] == self.curr_dir and self.curr_coords[1] > 0:
            return self.heat_map[self.curr_coords[0]][self.curr_coords[1] - 1]
        elif self.direction_atlas["DOWN"] == self.curr_dir and self.curr_coords[0] < len(self.heat_map) - 1:
            return self.heat_map[self.curr_coords[0] + 1][self.curr_coords[1]]
        else:
            return None
    
    def look_right(self) -> int:
        self.rotate_right()
        val = self.look_forward()
        self.rotate_left()
        return val

    def move_forward(self) -> bool:
        if self.look_forward() in (None, '9'):
            return False
        else:
            if self.direction_atlas["RIGHT"] == self.curr_dir:
                self.curr_coords = (self.curr_coords[0], self.curr_coords[1] + 1)
                return True
            elif self.direction_atlas["UP"] == self.curr_dir:
                self.curr_coords = (self.curr_coords[0] - 1, self.curr_coords[1])
                return True
            elif self.direction_atlas["LEFT"] == self.curr_dir:
                self.curr_coords = (self.curr_coords[0], self.curr_coords[1] - 1)
                return True
            elif self.direction_atlas["DOWN"] == self.curr_dir:
                self.curr_coords = (self.curr_coords[0] + 1, self.curr_coords[1])
                return True
    
    def get_forward_coord(self) -> tuple:
        if self.look_forward() is None:
            return None
        
        if self.direction_atlas["RIGHT"] == self.curr_dir:
            return (self.curr_coords[0], self.curr_coords[1] + 1)
        elif self.direction_atlas["UP"] == self.curr_dir:
            return (self.curr_coords[0] - 1, self.curr_coords[1])
        elif self.direction_atlas["LEFT"] == self.curr_dir:
            return (self.curr_coords[0], self.curr_coords[1] - 1)
        elif self.direction_atlas["DOWN"] == self.curr_dir:
            return (self.curr_coords[0] + 1, self.curr_coords[1])
    
    def get_right_coord(self) -> tuple:
        self.rotate_right()
        val = self.get_forward_coord()
        self.rotate_left()
        return val

    def get_basin_perimeter(self) -> list:
        perim_coords = set()

        # Go right till wall or out of bounds
        while self.move_forward(): pass
        start_perim_coords = self.curr_coords
        # Get all walls at start
        for _ in range(4):
            if self.look_forward() == '9':
                perim_coords.add(self.get_forward_coord())
            self.rotate_left()
        # Find first movement
        valid_dir = False
        while not valid_dir:
            if self.move_forward():
                valid_dir = True
            else:
                if self.look_forward() is not None:
                    perim_coords.add(self.get_forward_coord())
                self.rotate_left()
        # Follow perimeter till return to start
        while self.curr_coords != start_perim_coords:
            if self.look_right() is None:
                pass
            elif self.look_right() == '9':
                perim_coords.add(self.get_right_coord())
            else:
                self.rotate_right()
                self.move_forward()
                continue
            valid_dir = False
            while not valid_dir:
                if self.move_forward():
                    valid_dir = True
                else:
                    if self.look_forward() is not None:
                        perim_coords.add(self.get_forward_coord())
                    self.rotate_left()
        return sorted(list(perim_coords))

    def get_basin_area(self) -> int:
        perim_coords = self.get_basin_perimeter()
        print()
        for k, v in it.groupby(perim_coords, lambda x: x[0]):
            print(f"{k}: {list(v)}")

    




if __name__ == '__main__':
    main()