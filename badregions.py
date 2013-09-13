import math
import random

skyline = input("Skyline width? ")
maximum = input("max width? ")
smallest = input("smallest width? ")

skyline = int(skyline)
maximum = int(maximum)
smallest = int(smallest)

print('Bad region #1:')
print('1 -', smallest - 1)
print()

b1_low = 1
b1_hi = smallest - 1

ratio = maximum / smallest
print('Ratio:', ratio)
ratio = math.ceil(ratio)

ratio = math.ceil(maximum / smallest)
print('Ceil(Ratio):', ratio)


if maximum + 1 <= smallest * ratio - 1:
    print('Bad region #2:')
    if maximum + 1 == smallest * ratio - 1:
        print(maximum + 1)
        b2_low = maximum + 1
        b2_hi = maximum + 1
    else:
        print(maximum + 1, '-', smallest * ratio - 1)
        b2_low = maximum + 1
        b2_hi = smallest * ratio - 1
else:
    # There is no bad region #2
    b2_low = None
    b2_hi = None

print()


i = 0
while i < 100:
    i = i + 1
    n = random.randint(1, 100)
    if (n >= b1_low and n <= b1_hi) or (n >= b2_low and n <= b2_hi):
        print(n, 'Bad number')
    else:
        print(n)