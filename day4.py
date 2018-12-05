from inputreader import aocinput
from collections import defaultdict


class Guard:
    def __init__(self, id):
        self.id = id
        self.lastAsleep = None
        self.sleep = defaultdict(int)

    def fallAsleep(self, minute):
        self.lastAsleep = minute

    def wakeUp(self, minute):
        for i in range(self.lastAsleep, minute):
            self.sleep[i] += 1

    def totalSleep(self):  # total minutes asleep
        return sum(self.sleep.values())

    def maxSleepFrequency(self):  # maximum number of times asleep on a specific minute
        if self.sleep:
            return max(self.sleep.values())
        return 0

    def mostFrequentMinute(self):  # minute most frequently asleep
        if self.sleep:
            return max(self.sleep.items(), key=lambda item: item[1])[0]


def mostSleep(records):
    records.sort()  # sort records by time
    guards = {}
    activeGuard = None
    for record in records:
        if 'begins shift' in record:
            guardId = int(record.split()[-3][1:])
            if guardId in guards:
                activeGuard = guards[guardId]
            else:
                guards[guardId] = Guard(guardId)
                activeGuard = guards[guardId]
        elif 'falls asleep' in record:
            activeGuard.fallAsleep(int(record[15:17]))  # minute guard falls asleep
        elif 'wakes up' in record:
            activeGuard.wakeUp(int(record[15:17]))
    guards = list(guards.values())

    longest = max(guards, key=lambda guard: guard.totalSleep())

    frequent = max(guards, key=lambda guard: guard.maxSleepFrequency())

    return longest.id * longest.mostFrequentMinute(), frequent.id * frequent.mostFrequentMinute()


def main(day):
    data = aocinput(day)
    print(mostSleep(data))


if __name__ == '__main__':
    main(4)
