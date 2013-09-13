
# Author: Ian Wingate
# Ian_wingate_programming_project12.py
# Programming projects 1 & 2


n_str = input('What is n? ')
n_int = int(n_str)
variable = 2

output = 0
sum_of_outputs = 0
    
while n_int <= 64 and n_int:
    n_int = n_int
    output = variable**(n_int - 1)
    n_int = n_int + 1
    sum_of_outputs = sum_of_outputs + output

print()
print('There are',sum_of_outputs,'grains of wheat')
print()
weight = sum_of_outputs * 50

print('The weight is',weight,'mg')
print()
area_str = input('What is the area of the region in square kilometers? ')
area_int = int(area_str)
area_int= area_int * 10**12

volume_of_wheat_grain = 5 * 2 * 2

depth = volume_of_wheat_grain *  sum_of_outputs / area_int

print()
print('Volume =',volume_of_wheat_grain,'cubic millimeters')
print()
print('Depth is',depth,'mm')

depth = depth / 25.4

print()
print('Depth is', depth,'inches')
