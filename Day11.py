
import datetime
from pprint import pprint
import functools
import statistics
import pathlib


def main():
    begin_time = datetime.datetime.now()
    HOME = pathlib.Path(__file__).parent
    
    # Process input into octopuses
    with open(str(HOME) + "\\Day11Data.txt", "r") as fd:
        octopuses = [list(map(int, line)) for line in fd.read().splitlines()]
    
    count = 0
    steps = 10000
    for step in range(steps):
        # Increment the octo
        for i,line in enumerate(octopuses):
            for j, octopus in enumerate(line):
                octopuses[i][j] = octopus + 1
        # Cascade flashes
        flashed = [[False] * len(octopuses[0]) for _ in range(len(octopuses))]
        old_count = count + 1

        preflash = count
        while old_count != count:
            old_count = count
            for i, line in enumerate(octopuses):
                for j, octopus in enumerate(line):
                    if octopus > 9 and not flashed[i][j]:
                        flashed[i][j] = True
                        octopuses[i][j] = 0
                        count += 1
                        for k in range(9):
                            try:
                                if not flashed[i - 1 + k // 3][j - 1 + k % 3] and i - 1 + k // 3 >= 0 and j - 1 + k % 3 >= 0: 
                                    octopuses[i - 1 + k // 3][j - 1 + k % 3] += 1
                            except IndexError:
                                pass
        postflash = count
        if postflash - preflash == 100:
            print(f"Sim Flash: {step + 1}")
            break
    
    print(f"Flash Count: {count}")
    print(datetime.datetime.now() - begin_time)

if __name__ == '__main__':
    main()