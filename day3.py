from inputreader import aocinput
from collections import defaultdict


def multiclaim(claims):
    usedFabric = defaultdict(int)
    coordLists = getCoordLists(claims)

    for _, coordList in coordLists:
        for coord in coordList:
            usedFabric[coord] += 1

    overlapping = sum(map(lambda count: count > 1, usedFabric.values()))  # count coordinates used more than once

    for number, coordList in coordLists:
        if isIntact(usedFabric, coordList):
            return overlapping, number

    return None  # should never be able to reach this


def getCoordLists(claims):
    coordLists = []
    for claim in claims:
        number, _, coord, size = claim.split()
        number = int(number[1:])
        x, y = coord[:-1].split(',')
        w, h = size.split('x')
        coordList = [tuple([int(x) + i, int(y) + j]) for i in range(int(w)) for j in range(int(h))]
        coordLists.append([number, coordList])
    return coordLists


def isIntact(usedFabric, coordList):
    for coord in coordList:
        if usedFabric[coord] > 1:
            return False
    return True


def main(day):
    data = aocinput(day)
    print(multiclaim(data))


if __name__ == '__main__':
    main(3)
