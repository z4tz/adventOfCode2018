from inputreader import aocinput


def sumMetadata(data):
    metadata = []

    def node(start):
        nextEntry = start + 2  # read after child and metadata counts
        for i in range(data[start]):  # step through child nodes
            nextEntry = node(nextEntry)

        metadata.append(sum(data[nextEntry:nextEntry + data[start + 1]]))  # sum all metadata entries
        return nextEntry + data[start + 1]

    node(0)
    return sum(metadata)


def sumMetaData2(data):
    def node(start):
        nextEntry = start + 2  # read after child and metadata counts
        childSums = []
        for i in range(data[start]):  # step through child nodes
            nextEntry, childSum = node(nextEntry)
            childSums.append(childSum)

        metadata = 0
        if data[start] == 0:  # if no childnodes
             metadata = sum(data[nextEntry:nextEntry + data[start + 1]])  # sum all metadata entries
        else:
            for i in data[nextEntry:nextEntry + data[start + 1]]:  # for each metadata entry
                try:
                    metadata += childSums[i-1]
                except IndexError:
                    pass
        return nextEntry + data[start + 1], metadata

    return node(0)[1]


def main(day):
    data = list(map(int, aocinput(day)[0].split()))
    print(sumMetadata(data))
    print(sumMetaData2(data))


if __name__ == '__main__':
    main(8)
