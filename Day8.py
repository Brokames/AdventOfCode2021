
import datetime
import functools


def main():
    begin_time = datetime.datetime.now()

    # Process input into starting timers
    with open("C:\\Users\\Ja\\PycharmProjects\\AdventOfCode\\Day8Data.txt", "r") as fd:
        lines = fd.readlines()

    inp = [str(line.rstrip()).split(' | ')[0].split() for line in lines]
    out = [str(line.rstrip()).split(' | ')[1].split() for line in lines]
    count = 0
    total = 0
    for i in range(len(lines)):
        # Decode
        letter_map = {}
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            letter_map[letter] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        one = next((code for code in inp[i] if len(code) == 2))
        for letter in ('c', 'f'):
            letter_map[letter] = [l for l in letter_map[letter] if l in one]
        for k in letter_map:
            if k not in ('c', 'f'): letter_map[k] = [l for l in letter_map[k] if l not in letter_map['c']]
        seven = next((code for code in inp[i] if len(code) == 3))
        letter_map['a'] = [l for l in list(seven) if l not in one][0]
        for k in letter_map:
            if k != 'a' and letter_map['a'] in letter_map[k]: letter_map[k].remove(letter_map['a'])
        four = next((code for code in inp[i] if len(code) == 4))
        for letter in ('b', 'd'):
            letter_map[letter] = [l for l in list(four) if l not in letter_map['c']]
        for k in letter_map:
            if k not in ('b', 'd'): letter_map[k] = [l for l in letter_map[k] if l not in letter_map['b']]
        seven_count = [l for l in "abcdefg" if sum(l in s for s in inp[i]) == 7]
        for letter in ('d', 'g'):
            letter_map[letter] = [l for l in letter_map[letter] if l in seven_count]
        letter_map['b'] = [l for l in letter_map['b'] if l not in letter_map['d']]
        letter_map['e'] = [l for l in letter_map['e'] if l not in letter_map['g']]
        known_five = letter_map['a'][0] + letter_map['b'][0] + letter_map['d'][0] + letter_map['g'][0]
        five = next((code for code in inp[i] if len(code) == 5 and set(known_five) < set(code)))
        letter_map['f'] = [l for l in letter_map['f'] if l in five]
        letter_map['c'] = [l for l in letter_map['c'] if l not in letter_map['f']]
        letter_map = {k: v[0] for k,v in letter_map.items()}
        # Sum
        number_map = {
            tuple(sorted([letter_map['a'] , letter_map['b'] , letter_map['c'] , letter_map['e'] , letter_map['f'] , letter_map['g']])) : '0',
            tuple(sorted([letter_map['c'] , letter_map['f']])) : '1',
            tuple(sorted([letter_map['a'] , letter_map['c'] , letter_map['d'] , letter_map['e'] , letter_map['g']])) : '2',
            tuple(sorted([letter_map['a'] , letter_map['c'] , letter_map['d'] , letter_map['f'] , letter_map['g']])) : '3',
            tuple(sorted([letter_map['b'] , letter_map['c'] , letter_map['d'] , letter_map['f']])) : '4',
            tuple(sorted([letter_map['a'] , letter_map['b'] , letter_map['d'] , letter_map['f'] , letter_map['g']])) : '5',
            tuple(sorted([letter_map['a'] , letter_map['b'] , letter_map['d'] , letter_map['e'] , letter_map['f'] , letter_map['g']])) : '6',
            tuple(sorted([letter_map['a'] , letter_map['c'] , letter_map['f']])) : '7',
            ('a', 'b', 'c', 'd', 'e', 'f', 'g') : '8',
            tuple(sorted([letter_map['a'] , letter_map['b'] , letter_map['c'] , letter_map['d'] , letter_map['f'] , letter_map['g']])) : '9'
        }
        num = ""
        for d in out[i]:
            d = tuple(sorted(list(d)))
            num += number_map[d]
        total += int(num)
    
    print(total)

    print(datetime.datetime.now() - begin_time)

if __name__ == '__main__':
    main()