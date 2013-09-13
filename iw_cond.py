#Author Ian W
#Project D


while True:
    n, m = input().split()
    if n == m == '0':
        break
    print(n,m)
    other_lines = 1
    while other_lines <= 3:
        k = input()
        print([k])
        other_lines += 1
    
