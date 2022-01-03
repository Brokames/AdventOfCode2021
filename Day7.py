
import datetime
import functools


def main():
    begin_time = datetime.datetime.now()

    # Process input into starting timers
    with open("C:\\Users\\Ja\\PycharmProjects\\AdventOfCode\\Day7Data.txt", "r") as fd:
        start_pos = list(map(int,fd.read().split(',')))
    
    min_cost = 1000000000
    for i in range(min(start_pos), max(start_pos) + 1):
        total = sum(map(lambda x: linear_fuel(abs(x - i)), start_pos))
        if total < min_cost:
            min_cost = total
            min_pos = i

    print(min_pos)
    print(sum(map(lambda x: linear_fuel(abs(x - min_pos)), start_pos)))

    print(datetime.datetime.now() - begin_time)

@functools.cache
def linear_fuel(distance):
    total = 0
    for i in range(distance):
        total += i + 1
    return total

if __name__ == '__main__':
    main()