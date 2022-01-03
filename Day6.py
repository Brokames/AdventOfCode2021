
import datetime
import functools


def main():
    begin_time = datetime.datetime.now()

    # Process input into starting timers
    with open("C:\\Users\\Ja\\PycharmProjects\\AdventOfCode\\Day6Data.txt", "r") as fd:
        lines = fd.readlines()
    curr_timers = lines[0].split(',')
    curr_timers = [int(element) for element in curr_timers]

    # curr_timers = [3,4,3,1,2]
    # Decrement timers and make new fish
    num_days = 2048
    # Old Method
    """for i in range(num_days):
        new_fish = 0
        for i in range(len(curr_timers)):
            curr_timers[i] -= 1
            if curr_timers[i] == -1:
                curr_timers[i] = 6
                new_fish += 1
        curr_timers += [8] * new_fish
        total_fish = curr_timers"""

    # New Method
    total_fish = sum(num_new_fish(fish, num_days - 1) for fish in curr_timers)

    print(total_fish)
    
    print(datetime.datetime.now() - begin_time)


@functools.lru_cache(maxsize=1024)
def num_new_fish(start_timer, days):
    if start_timer > days:
        return 1
    return num_new_fish(7, days - start_timer) + num_new_fish(9, days - start_timer)


if __name__ == '__main__':
    main()