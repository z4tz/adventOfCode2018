from inputreader import aocinput
import numpy as np
from itertools import cycle

# NOTE TO SELF: numpy arrays are accessed as [y, x]


class Cart:
    cartDirections = {'^': np.array([-1, 0]),
                      '>': np.array([0, 1]),
                      'v': np.array([1, 0]),
                      '<': np.array([0, -1])}

    def __init__(self, coords, direction, grid):
        self.coords = coords
        self.direction = self.cartDirections[direction]
        self.grid = grid
        self.intersect = cycle([self.turnLeft,
                                lambda: None,
                                self.turnRight])

    def move(self):
        self.coords += self.direction
        square = self.grid.item(*self.coords)
        if square == '+':
            next(self.intersect)()
        elif square == '\\':
            self.direction = np.flip(self.direction)
        elif square == '/':
            self.direction = np.flip(self.direction) * -1

    def turnLeft(self):
        self.direction = np.flip(self.direction) * np.array([-1, 1])

    def turnRight(self):
        self.direction = np.flip(self.direction) * np.array([1, -1])


def findCollision(data):
    lineLength = max([len(line) for line in data])
    data = [list(line.strip('\n') + ' ' * (lineLength - len(line))) for line in data]
    grid = np.array(data)
    carts = []
    for y, x in zip(*np.where(np.isin(grid, ['^', '>', 'v', '<']))):
        carts.append(Cart(np.array([y, x], int), grid[y, x], grid))

    firstCrash = None
    while len(carts) > 1:
        toRemove = []
        carts.sort(key=lambda c: (c.coords[0], c.coords[1]))
        for cart in carts:
            cart.move()
            for otherCart in carts:
                if np.equal(otherCart.coords, cart.coords).all() and otherCart is not cart:
                    if firstCrash is None:
                        firstCrash = cart.coords
                    toRemove.extend([cart, otherCart])
        for cart in toRemove:
            carts.remove(cart)

    return np.flip(firstCrash), np.flip(carts[0].coords)


def main(day):
    data = aocinput(day)
    print(findCollision(data))


if __name__ == '__main__':
    main(13)
