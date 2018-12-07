from inputreader import aocinput
from collections import defaultdict


def largestAreas(coords):
    coords = [tuple(int(part) for part in line.split(',')) for line in coords]
    xmax = max(coords, key=lambda item: item[0])[0]
    xmin = min(coords, key=lambda item: item[0])[0]
    ymax = max(coords, key=lambda item: item[1])[1]
    ymin = min(coords, key=lambda item: item[1])[1]

    dangerAreas = defaultdict(int)
    disqualified = set()
    areas = [[x, y] for x in range(xmin, xmax + 1) for y in range(ymin, ymax + 1)]

    for area in areas:
        closest = closestDanger(coords, area)
        if closest not in disqualified:
            if xmax == area[0] or xmin == area[0] or ymax == area[1] or ymin == area[1]:
                disqualified.add(closest)
            else:
                dangerAreas[closest] += 1

    for disq in disqualified:
        if disq in dangerAreas:
            del dangerAreas[disq]

    #part 2
    safeAreaSize = sum([closeEnough(coords, area) for area in areas])

    return max(dangerAreas.values()), safeAreaSize


def distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])


def closestDanger(dangers, area):
    closest = [None, float('inf')]
    for danger in dangers:
        dist = distance(danger, area)
        if dist < closest[1]:
            closest = [danger, dist]
        elif dist == closest[1]:
            closest = [None, dist]
    return closest[0]


def closeEnough(coords, area):
    totDistance = 0
    for coord in coords:
        totDistance += distance(area, coord)
        if totDistance >= 10000:
            return False
    return True


def main(day):
    data = aocinput(day)
    print(largestAreas(data))


if __name__ == '__main__':
    main(6)
