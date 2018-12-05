from inputreader import aocinput
import string


def polyReduce(line):
    prevline = ''
    while line != prevline:
        prevline = line
        for lower, upper in zip(string.ascii_lowercase, string.ascii_uppercase):
            line = line.replace(lower + upper, '').replace(upper + lower, '')
    return len(line)


def improvedPoly(line):
    return min([polyReduce(line.replace(char, '').replace(char.upper(), '')) for char in string.ascii_lowercase])


def main(day):
    data = aocinput(day)[0].strip()
    print(polyReduce(data))
    print(improvedPoly(data))


if __name__ == '__main__':
    main(5)
