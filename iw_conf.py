# Author Ian W
# Project F

while True:
    n = int(input())
    if n == 0:
        break
    print(n)
    z = 1
    while z <= n:
        a, b, c, d = input().split()
        x1 = int(a)
        y1 = int(b)
        x2 = int(c)
        y2 = int(d)
        print('({}, {}) ({}, {})'. format(x1, y1, x2, y2))
        z += 1
