import random
i = 0
while i < 600:
    n = random.randint(30,49)
    value = i + n
    while value < 30 or (value > 49 and value < 60):
        n = random.randint(30,49)
    i = i + n
    print(n)
print(i)
	