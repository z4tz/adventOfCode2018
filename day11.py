from inputreader import aocinput
import numpy as np


def findCell(serial,):
    grid = np.zeros([300, 300])
    for x, y in np.ndindex(grid.shape):  # x, y 0->299, add 1 when correct coord is needed
        grid[x, y] = int(str((((x + 1) + 10) * (y + 1) + serial) * ((x + 1) + 10))[-3])-5

    def calcMaxPower(squaresize):
        powers = []
        for x in range(grid.shape[0] - squaresize + 1):
            for y in range(grid.shape[1] - squaresize + 1):
                powers.append([np.sum(grid[x:x + squaresize, y:y + squaresize]), [x + 1, y + 1]])
        return max(powers, key=lambda item: item[0])

    maxPowers = [[*calcMaxPower(squaresize), squaresize]for squaresize in range(1, 22)]

    return maxPowers[2][1], max(maxPowers, key=lambda item: item[0])[1:]


def main(day):
    data = aocinput(day)
    print(findCell(int(data[0])))


if __name__ == '__main__':
    main(11)
