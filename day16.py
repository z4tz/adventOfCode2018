from inputreader import aocinput
from collections import namedtuple, defaultdict

class operators:

    @staticmethod
    def addr(a, b, c, reg):
        reg[c] = reg[a] + reg[b]

    @staticmethod
    def addi(a, b, c, reg):
        reg[c] = reg[a] + b

    @staticmethod
    def mulr(a, b, c, reg):
        reg[c] = reg[a] * reg[b]

    @staticmethod
    def muli(a, b, c, reg):
        reg[c] = reg[a] * b

    @staticmethod
    def banr(a, b, c, reg):
        reg[c] = reg[a] & reg[b]

    @staticmethod
    def bani(a, b, c, reg):
        reg[c] = reg[a] & b

    @staticmethod
    def borr(a, b, c, reg):
        reg[c] = reg[a] | reg[b]

    @staticmethod
    def bori(a, b, c, reg):
        reg[c] = reg[a] | b

    @staticmethod
    def setr(a, b, c, reg):
        reg[c] = reg[a]

    @staticmethod
    def seti(a, b, c, reg):
        reg[c] = a

    @staticmethod
    def gtir(a, b, c, reg):
        reg[c] = int(a > reg[b])

    @staticmethod
    def gtri(a, b, c, reg):
        reg[c] = int(reg[a] > b)

    @staticmethod
    def gtrr(a, b, c, reg):
        reg[c] = int(reg[a] > reg[b])

    @staticmethod
    def eqir(a, b, c, reg):
        reg[c] = int(a == reg[b])

    @staticmethod
    def eqri(a, b, c, reg):
        reg[c] = int(reg[a] == b)

    @staticmethod
    def eqrr(a, b, c, reg):
        reg[c] = int(reg[a] == reg[b])


Testcase = namedtuple('Testcase', ['initial', 'values', 'result'])


def multibehave(data):
    methods = [getattr(operators, func)for func in dir(operators) if callable(getattr(operators, func)) and not func.startswith("__")]
    testcases = getTestcases(data)

    multicodes = 0
    for i, testcase in enumerate(testcases):
        correct = 0
        for method in methods:
            initial = testcase.initial[:]
            method(*testcase.values[1:], initial)
            if initial == testcase.result:
                correct += 1
        if correct >= 3:
            multicodes += 1
    return multicodes


def getTestcases(data):
    testcases = []

    for i in range(0, int(len(data)), 4):
        initial = [int(num) for num in data[i][9:19].split(', ')]
        values = [int(num) for num in data[i+1].split()]
        result = [int(num) for num in data[i+2][9:19].split(', ')]
        testcases.append(Testcase(initial, values, result))
    return testcases


def testprogram(data1, data2):
    methods = [getattr(operators, func)for func in dir(operators) if callable(getattr(operators, func)) and not func.startswith("__")]
    testcases = getTestcases(data1)

    possibleCodes = defaultdict(set)

    for testcase in testcases:
        for method in methods:
            initial = testcase.initial[:]
            method(*testcase.values[1:], initial)
            if initial == testcase.result:
                possibleCodes[method].add(testcase.values[0])

    correctcodes = {}
    while possibleCodes:
        for method, codes in dict(possibleCodes).items():
            if len(codes) == 1:
                code = codes.pop()
                correctcodes[code] = method
                del possibleCodes[method]
                for arr in possibleCodes.values():
                    if code in arr:
                        arr.remove(code)

    register = [0, 0, 0, 0]
    for values in data2:
        values = [int(value) for value in values.split()]
        correctcodes[values[0]](*values[1:], register)

    return register[0]

def main(day):
    data = [line.strip() for line in aocinput(day)]
    data1 = data[:3124]
    data2 = data[3126:]
    print(multibehave(data1))
    print(testprogram(data1, data2))


if __name__ == '__main__':
    main(16)
