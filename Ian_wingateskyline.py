

# Ian_Wingateskyline.py
# Second attempt at Skyline Program
# Author: Ian Wingate

skyline_str = input('What width is the Skyline? ')  
large_building_str = input('What width the largest building? ')
small_building_str = input('What width is the smallest building? ')
skyline_int = int(skyline_str)
large_building_int = int(large_building_str)
small_building_int = int(small_building_str)


import random
value = 0
remainder = skyline_int
while value < skyline_int:
    n = random.randint(small_building_int, large_building_int)
    value = value + n
    remainder = remainder - n
    print(n)
    if remainder > 0 and remainder < small_building_int:
        value = value - n
        remainder = remainder + n
    if remainder > large_building_int and remainder < 2 * small_building_int:
        value = value - n
        remainder = remainder + n
    if remainder < small_building_int and remainder != 0: 
        value = value - n
        remainder = remainder + n
print(value)
