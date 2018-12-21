from inputreader import aocinput
import numpy as np
import re


def buildworld(data):
    clay = set()
    regex = re.compile('^([xy])=([0-9]*), [xy]=([0-9]*)..([0-9]*)')
    for line in data:
        match = regex.match(line)
        static = int(match.group(2))
        for variable in range(int(match.group(3)), int(match.group(4)) + 1):
            if match.group(1) == 'x':
                clay.add((static, variable))
            else:
                clay.add((variable, static))

    xmin = min(clay, key=lambda c: c[0])[0]
    xmax = max(clay, key=lambda c: c[0])[0]
    ymin = min(clay, key=lambda c: c[1])[1]
    ymax = max(clay, key=lambda c: c[1])[1]

    world = np.empty([ymax - ymin + 1, xmax - xmin + 3], dtype=str)
    world[:] = '.'
    for x, y in clay:
        world[y - ymin, x - xmin + 1] = '#'
    return world, xmin


def display(world):
    np.set_printoptions(threshold=10000000, linewidth=5000)
    print('\n')
    print(str(world).replace(' ', '').replace('[', '').replace(']', '').replace('\'', ''))


def waterReach(data):

    def water(start):
        x = start[0]
        y = start[1]
        while world[y + 1, x] == '.':
            if y >= waterLimit - 2:
                for yfall in range(start[1], y + 2):
                    world[yfall, x] = '|'
                return
            y += 1
        if world[y + 1, x] == '|':
            for yfall in range(start[1], y + 1):
                world[yfall, x] = '|'
            return

        while bound(x, y):
            y -= 1

        for yfall in range(start[1], y+1):
            world[yfall, x] = '|'

        for x, y in unbound(x, y):
            water((x, y))
        return

    def bound(x, y):
        xl = x
        xr = x
        while world[y, xl - 1] not in '#~':
            xl -= 1
            if world[y + 1, xl] not in '#~':
                return False
        while world[y, xr + 1] not in '#~':
            xr += 1
            if world[y + 1, xr] not in '#~':
                return False

        for x in range(xl, xr+1):
            world[y, x] = '~'
        return True

    def unbound(x, y):
        xl = x
        xr = x
        falls = []
        while world[y, xl - 1] not in '#~':
            xl -= 1
            if world[y + 1, xl] not in '#~':
                falls.append((xl, y+1))
                break
        while world[y, xr + 1] not in '#~':
            xr += 1
            if world[y + 1, xr] not in '#~':
                falls.append((xr, y+1))
                break
        for x in range(xl, xr+1):
            world[y, x] = '|'
        return falls

    world, xmin = buildworld(data)
    waterLimit = world.shape[0]

    water((500-xmin + 1, 0))
    #display(world)
    return sum(sum(np.isin(world, ['~', '|']))), sum(sum(np.isin(world, ['~'])))


def main(day):
    data = aocinput(day)
    print(waterReach(data))


if __name__ == '__main__':
    main(17)
