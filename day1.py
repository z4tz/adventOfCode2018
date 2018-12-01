from inputreader import aocinput
from itertools import cycle


def freqSum(frequencies):
    return sum([frequency for frequency in frequencies])


def findRepeat(frequencies):
    currentFreq = 0
    used = set()
    for frequency in cycle(frequencies):
        used.add(currentFreq)
        currentFreq += frequency
        if currentFreq in used:
            return currentFreq


def main(day):
    data = [int(item) for item in aocinput(day)]
    print(freqSum(data))
    print(findRepeat(data))


if __name__ == '__main__':
    main(1)
