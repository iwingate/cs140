# Author: Ian Wingate
# iw_PP4.py
# Programming Project 4

A_str = input('What is A? ')
B_str = input('What is B? ')

A = int(A_str)
B = int(B_str)

product = 0

if B % 2 == 1:
    product = product + A

while B > 1: 
    A = A * 2
    B = B // 2
    if B % 2 == 1:
        product = product + A
    if B == 1:
        print(product) 
        A_str = input('What is A? ')
        B_str = input('What is B? ')
        A = int(A_str)
        B = int(B_str)
        product = 0
        if B % 2 == 1:
            product = product + A
            continue
    else: 
        continue   



    
   
    