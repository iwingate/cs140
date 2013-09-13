# Author Ian W
# Project E

while True:
    n, m = input().split()
    if n == m == '0':
        break
    print(n, m)
    z = 1
    m = int(m)
    while z <= m:
        m_lines = input().split()
        first = m_lines[0]
        second = m_lines[1]
        third = m_lines[2]
        z += 1
        print('{} to building {}, costs {} units'.format(first, second, third))

	
