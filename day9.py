from inputreader import aocinput
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self, iterable=None):
        self.startNode = None
        self.currentNode = None
        if iterable:
            for item in iterable:
                self.add(item)
            self.rotate(1)

    def append(self, data):
        if self.currentNode is None:
            self.currentNode = Node(data)
            self.currentNode.prev = self.currentNode
            self.currentNode.next = self.currentNode
            self.startNode = self.currentNode
        else:
            node = Node(data)
            node.prev = self.currentNode
            node.next = self.currentNode.next
            node.next.prev = node
            self.currentNode.next = node

    def add(self, data):
        self.append(data)
        self.rotate(1)

    def rotate(self, steps=1):
        if self.currentNode:
            if steps > 0:
                for _ in range(steps):
                    self.currentNode = self.currentNode.next
            elif steps < 0:
                for _ in range(abs(steps)):
                    self.currentNode = self.currentNode.prev

    def pop(self):
        if self.currentNode:
            data = self.currentNode.data
            prev = self.currentNode.prev
            next = self.currentNode.next
            prev.next = next
            next.prev = prev
            self.currentNode = next
            return data

    def __repr__(self):
        node = self.startNode
        items = [node.data]
        node = node.next
        while node is not self.startNode:
            items.append(node.data)
            node = node.next
        return items.__str__()


class LinkedListOptimized:
    def __init__(self, iterable=None):
        self.startNode = None
        self.currentNode = None
        if iterable:
            for item in iterable:
                self.add(item)
            self.rotate(1)

    def append(self, data):
        if self.currentNode is None:
            self.currentNode = [None, data, None]
            self.currentNode[0] = self.currentNode
            self.currentNode[2] = self.currentNode
            self.startNode = self.currentNode
        else:
            node = [self.currentNode, data, self.currentNode[2]]
            node[2][0] = node
            self.currentNode[2] = node

    def add(self, data):
        self.append(data)
        self.rotate(1)

    def rotate(self, steps=1):
        if steps > 0:
            for _ in range(steps):
                self.currentNode = self.currentNode[2]
        elif steps < 0:
            for _ in range(abs(steps)):
                self.currentNode = self.currentNode[0]

    def pop(self):
        node = self.currentNode
        node[0][2] = node[2]
        node[2][0] = node[0]
        self.currentNode = node[2]
        return node[1]

    def __repr__(self):
        node = self.startNode
        items = [node[1]]
        node = node[2]
        while node is not self.startNode:
            items.append(node[1])
            node = node[2]
        return items.__str__()


def marbleGame(data, multiple=1):
    players = int(data[0].split()[0])
    lastMarble = int(data[0].split()[6]) * multiple
    marbles = deque([0])
    score = [0]*players
    for turn in range(1, lastMarble + 1):
        if turn % 23 == 0:
            marbles.rotate(-7)
            score[(turn - 1) % players] += turn + marbles.pop()
        else:
            marbles.rotate(2)
            marbles.append(turn)

    return max(score)


def main(day):
    data = aocinput(day)
    print(marbleGame(data))
    print(marbleGame(data, 100))


if __name__ == '__main__':
    main(9)
