
import datetime
from pprint import pprint
import functools
import statistics


def main():
    begin_time = datetime.datetime.now()

    # Process input into starting timers
    with open("C:\\Users\\Ja\\PycharmProjects\\AdventOfCode\\Day10Data.txt", "r") as fd:
        lines = fd.readlines()
    for i, line in enumerate(lines):
        lines[i] = str(line).rstrip()
    
    ref_dict = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    

    correct_lines = lines.copy()

    syntax_issue = []
    for line in lines:
        stack = []
        for brace in line:
            if brace in ('(', '[', '{', '<'):
                stack.append(brace)
            else:
                if ref_dict[brace] != stack[-1]:
                    correct_lines.remove(line)
                    syntax_issue.append(brace)
                    break
                stack.pop()

    scores = []
    for line in correct_lines:
        stack = []
        for brace in line:
            if brace in ('(', '[', '{', '<'):
                stack.append(brace)
            else:
                stack.pop()
        complete_string = ""
        rev_ref_dict = {v:k for k, v in ref_dict.items()}
        for brace in stack[::-1]:
            complete_string += rev_ref_dict[brace]
        score = 0
        for brace in complete_string:
            score *= 5
            if brace == ')': score += 1
            elif brace == ']': score += 2
            elif brace == '}': score += 3
            else: score += 4
        scores.append(score)
    
    print(statistics.median(scores))


    corrupt_total = 0
    for brace in syntax_issue:
        if brace == ')': corrupt_total += 3
        elif brace == ']': corrupt_total += 57
        elif brace == '}': corrupt_total += 1197
        else: corrupt_total += 25137
    print(f"Corrupt total: {corrupt_total}")
                
    print(datetime.datetime.now() - begin_time)

if __name__ == '__main__':
    main()