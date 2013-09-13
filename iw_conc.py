# Author: Ian W
# Project C


while True:
    m, n = input().split()
    if m == '0':
        break
    print(m, n)
    k = int(input())
    print(k)
    z = 1
    set = []
    while z <= k:
        k_sub = input()
        z += 1
        print([k_sub])
