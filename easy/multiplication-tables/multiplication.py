import sys

for i in range(1,13):
    print '{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'.format(*[x * i for x in range(1,13)]).rstrip().strip()

