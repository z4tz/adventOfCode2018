from inputreader import aocinput
from collections import defaultdict
import numpy as np


def countPlants(data):
    pots = defaultdict(lambda: '.', enumerate(data[0].split()[-1]))  # {position: #/.}
    growthTable = defaultdict(lambda: '.', (line.strip().split(' => ') for line in data[2:]))

    values = []
    # end when constant increase detected, len(..) < 3 to prevent early end
    while len(set(np.diff(values[-5:]))) > 1 or len(values) < 3:

        newpots = defaultdict(lambda: '.')
        for i in range(min(pots.keys())-2, max(pots.keys())+2):
            newpots[i] = growthTable[''.join([pots[j] for j in range(i-2, i+3)])]
        pots = newpots

        values.append(sum([item[0] for item in pots.items() if item[1] == '#']))

    return values[19], values[-1] + np.diff(values[-2:])[0] * (50000000000 - len(values))



def main(day):
    data = aocinput(day)
    print(countPlants(data))


if __name__ == '__main__':
    main(12)
