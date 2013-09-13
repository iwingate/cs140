# Author: Ian Wingate
# Project 11108
# http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=23&page=show_problem&problem=2049
# Synopsis: Logic Game with dice, 'WFF 'N PROOF'

# Set a variable n as our counter for Cases
n = 0
#While loop to process all data available
while True:
    n += 1
    print('Case {}'.format(n))
 
# Set or list creation
    set = []
    data = list(input())
    set = set + data
    print(set)
