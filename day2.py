from inputreader import aocinput
from collections import defaultdict


def checksum(IDs):
    twos = 0
    threes = 0
    for ID in IDs:
        chardict = defaultdict(int)
        for char in ID:
            chardict[char] += 1
        if 2 in chardict.values():
            twos += 1
        if 3 in chardict.values():
            threes += 1
    return twos * threes


def commonLetters(IDs):
    for i in range(len(IDs[0])):
        reduced = list(map(lambda x: x[:i] + x[i+1:], IDs))  # remove char at position i
        unique = set(reduced)
        if not len(unique) == len(reduced):
            for string in unique:
                reduced.remove(string)
            return reduced[0]


def main(day):
    data = [line.strip() for line in aocinput(day)]
    print(checksum(data))
    print(commonLetters(data))


if __name__ == '__main__':
    main(2)
