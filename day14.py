from inputreader import aocinput
from collections import deque


def recipe(data):
    dataArray = deque([int(char) for char in data])
    data = int(data)
    bell = 0
    joy = 1
    board = [3, 7]
    boardEnd = deque(board, maxlen=len(dataArray))
    part1 = None
    part2 = None
    while not part1 or not part2:
        scores = [int(char) for char in str(board[bell] + board[joy])]
        for score in scores:
            board.append(score)
            boardEnd.append(score)
            if boardEnd == dataArray and not part2:
                part2 = len(board) - len(dataArray)
                print('part2')
        boardLen = len(board)
        bell = (bell + board[bell] + 1) % boardLen
        joy = (joy + board[joy] + 1) % boardLen
        if not part1 and boardLen >= data + 10:
            part1 = ''.join([str(number) for number in board[data:data+10]])
            print('part1')

    return part1, part2


def main(day):
    data = aocinput(day)
    print(recipe(data[0]))


if __name__ == '__main__':
    main(14)
