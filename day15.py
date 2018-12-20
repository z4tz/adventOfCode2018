from inputreader import aocinput


class Unit:
    def __init__(self, x, y, type, attack):
        self.hp = 200
        self.x = x
        self.y = y
        self.type = type
        self.attack = attack

    def squaresInRange(self, grid):
        """return list of coords where an enemy can stand and attack from"""
        return [coord for coord in nearbyCoords(self.coord) if coord in grid]

    def moveTo(self, coord):
        self.x = coord[0]
        self.y = coord[1]

    def __repr__(self):
        return f'{self.type} ({self.x},{self.y}) HP:{self.hp}'

    def __lt__(self, other):
        # sorting of units in read order
        if self.y < other.y:
            return True
        if self.y == other.y and self.x < other.x:
            return True
        return False

    @property
    def coord(self):
        return self.x, self.y


def combat(data, elfAttack=3):
    basegrid = set()  # coordinates that are free without considering unit positions
    elves = set()
    goblins = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char in ['.', 'G', 'E']:
                basegrid.add((x, y))
            if char == 'E':
                elves.add(Unit(x, y, 'Elf', elfAttack))
            if char == 'G':
                goblins.add(Unit(x, y, 'Goblin', 3))
    turn = 0
    elfDied = False
    while True:
        allunits = sorted([*elves, *goblins])  # units in turn order
        for unit in allunits[:]:  # copy of allunits to not have it modified when units die during turn
            if unit.hp <= 0:
                continue  # avoid dead unit acting
            if elves and goblins:  # combat is not over
                currentGrid = set(basegrid)
                for u in allunits:
                    currentGrid.remove(u.coord)

                if unit.type == 'Elf':
                    enemies = goblins
                else:
                    enemies = elves

                target = findTargetInRange(unit, enemies)
                if not target:  # if no target, try to move closer to one
                    moveUnit(unit, enemies, currentGrid)
                    target = findTargetInRange(unit, enemies)

                if target:
                    target.hp -= unit.attack
                    if target.hp <= 0:  # remove dead units
                        allunits.remove(target)
                        if target.type == 'Elf':
                            elfDied = True
                            elves.remove(target)
                        else:
                            goblins.remove(target)

            else:
                # combat is over
                if elves:
                    return sum([elf.hp for elf in elves]) * turn, elfDied
                else:
                    return sum([goblin.hp for goblin in goblins]) * turn, elfDied

        turn += 1


def moveUnit(unit, enemies, grid):
    """Attempt to move unit. If no valid targets are found, stand still"""
    # get nonblocked squares around enemies
    attackSquares = [availableCoord for enemy in enemies for availableCoord in enemy.squaresInRange(grid)]
    # attackSquares reachable from current location with the shortest distance
    reachableAttackSquares = [coord for coord in distances(grid, unit.coord, attackSquares) if coord in attackSquares]
    if reachableAttackSquares:
        closestAttackSquare = sorted(reachableAttackSquares, key=lambda t: (t[1], t[0]))[0]
        dists = distances(grid, closestAttackSquare, nearbyCoords(unit.coord))
        # filter out locations that was not reachable from closestAttackSquare
        possibleMoves = [move for move in unit.squaresInRange(grid) if move in dists]
        possibleMoves.sort(key=lambda coord: (dists[coord], coord[1], coord[0]))  # distance then read order
        unit.moveTo(possibleMoves[0])


def findTargetInRange(unit, enemies):
    """Returns enemy in range for attack
    If multiple enemies are in range return the one with lowest hp, in case of a draw read order decides
    """
    enemiesInRange = [enemy for enemy in enemies if enemy.coord in nearbyCoords(unit.coord)]
    enemiesInRange.sort(key=lambda enemy: (enemy.hp, enemy.y, enemy.x))
    return enemiesInRange[0] if enemiesInRange else None


def nearbyCoords(coord):
    """Returns list of coordinates that are one step up, down, left and right of given coordinate"""
    return [((coord[0]-1), coord[1]), ((coord[0]), coord[1]-1), ((coord[0]), coord[1]+1), ((coord[0]+1), coord[1])]


def distances(grid, start, targets=None):
    """
    Breadth First Search
    :param grid: set of all coordinates available
    :param start: start coordinate on format: (x, y)
    :param targets: list of coordinates that will end the search, coordinates at the same distance will be calculated
    :return : dictionary of all reachable coordinates and the distance to them on format {coordinate: distance}
    """
    distance = 0
    toVisit = [start]
    distances = dict()
    if not targets:
        targets = []
    targetFound = False
    while not targetFound and toVisit:
        newLocations = set()
        for coord in toVisit:
            # add new coordinate if it's a valid location and it has not yet been visited
            newLocations.update([newcoord for newcoord in nearbyCoords(coord) if newcoord in grid and not newcoord in distances])
            distances[coord] = distance
            if coord in targets:
                targetFound = True
        toVisit = newLocations
        distance += 1
    return distances


# part 1
def combatResult(data):
    return combat(data)[0]


# part 2
def noElfDies(data):
    elfAttack = 3
    deadElf = True
    while deadElf:
        elfAttack += 1
        result, deadElf = combat(data, elfAttack)
    return result


def main(day):
    data = [line.strip() for line in aocinput(day)]
    print(combatResult(data))
    print(noElfDies(data))


if __name__ == '__main__':
    main(15)
