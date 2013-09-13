# Author: Ian Wingate
# PP_2.py
# A program to measure thickness of folds


number_folds_str = input('Enter the number of folds: ')
number_folds_int = int(number_folds_str)

thickness = number_folds_int * 1/200
print('The thickness is',thickness, 'cm')

in_meters = thickness * .01 
print('or',in_meters, 'meters')