import timeit
import os

days = range(1, len(os.listdir('inputs/')) + 1)
runs = 1


def setupstring(day):
    return """
from day{0} import main
day = {0}""".format(day)


for day in days:
    print("-----## Assignment day {0} ##-----".format(day))
    print("Time used for assignment {0}: {1}s\n\n".format(day, timeit.timeit("main(day)", setup=setupstring(day),
                                                                             number=runs) / runs))
