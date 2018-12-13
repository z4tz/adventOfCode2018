from inputreader import aocinput
import matplotlib.pyplot as plt
import re


def displayMessage(data):
    X = []
    Y = []
    VX = []
    VY = []

    regex = re.compile('<([ 0-9\-]+),([ 0-9\-]+)> velocity=<([ 0-9\-]+),([ 0-9\-]+)>')
    for item in data:
        groups = regex.search(item).groups()
        X.append(int(groups[0]))
        Y.append(int(groups[1]))
        VX.append(int(groups[2]))
        VY.append(int(groups[3]))

    spread = max(Y) - min(Y)
    oldSpread = spread
    count = 0
    while spread <= oldSpread:
        for i in range(len(X)):
            X[i] += VX[i]
            Y[i] += VY[i]
        oldSpread = spread
        spread = max(Y) - min(Y)
        count += 1
    # take one step back
    for i in range(len(X)):
        X[i] -= VX[i]
        Y[i] -= VY[i]
    count -= 1

    plt.scatter(X, Y)
    plt.gca().invert_yaxis()
    plt.gcf().set_size_inches(6, 1.5, forward=True)
    #plt.show()
    print('Part 1 answer generated but not displayed')
    return count


def main(day):
    data = aocinput(day)
    print(displayMessage(data))


if __name__ == '__main__':
    main(10)
