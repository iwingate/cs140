# Author Ian W
# Project G 


n = 0   
while n <= 1000:
    n = int(input())
    z = 1
    if n == 0:
        break
    print('Test Case')
    while z <= n:
        a, b = input().split()
        x = int(a)
        y = int(b)
        print('({}, {})'.format(x, y))
        z += 1
