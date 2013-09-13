import random
value = 0
remainder = 600
while value < 600:
    n = random.randint(30, 49)
    value = value + n
    remainder = remainder - n
    print(n)
    if remainder > 0 and remainder < 30:
        value = value - n
        remainder = remainder + n
    if remainder > 49 and remainder < 60:
        value = value - n
        remainder = remainder + n
    if remainder < 30 and remainder != 0: 
        value = value - n
        remainder = remainder + n
print(value)
