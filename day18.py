from inputreader import aocinput
import numpy as np


def forestmagic(data):
    forest = np.array([list(line.strip()) for line in data], dtype=str)
    newForest = np.copy(forest)
    values = []
    repeat = 0
    while repeat < 3:
        for x, y in np.ndindex(forest.shape):
            if forest[y, x] == '.' and np.count_nonzero(nearby(x, y, forest) == '|') >= 3:
                newForest[y, x] = '|'
            elif forest[y, x] == '|' and np.count_nonzero(nearby(x, y, forest) == '#') >= 3:
                newForest[y, x] = '#'
            elif forest[y, x] == '#':
                # nearby also includes the centre, check for 2 '#' instead of just one
                if np.count_nonzero(nearby(x, y, forest) == '#') >= 2 and '|' in nearby(x, y, forest):
                    newForest[y, x] = '#'
                else:
                    newForest[y, x] = '.'

        forest = np.copy(newForest)
        value = np.count_nonzero(forest == '|') * np.count_nonzero(forest == '#')
        if value in values:
            repeat += 1
        else:
            repeat = 0
        values.append(value)

    period = len(values) - 1 - values.index(values[-1])
    # index of repeating value + steps forward (within the periodicity)
    index = values.index(values[-1]) + (1000000000 - (values.index(values[-1]) + 1)) % period
    return values[index]


def nearby(x, y, array):
    return array[max(0, y - 1):y + 2, max(0, x - 1):x + 2]


def display(array):
    np.set_printoptions(threshold=10000000, linewidth=5000)
    print(str(array).replace(' ', '').replace('[', '').replace(']', '').replace('\'', ''))
    print('\n')


def main(day):
    data = aocinput(day)
    print(forestmagic(data))


if __name__ == '__main__':
    main(18)
