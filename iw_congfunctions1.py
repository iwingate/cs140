# Author Ian W
# Project G 

def main():
    case_line = 0
    while True:
        case_size = int(input())
        if case_size == 0:
            break
        data = read_case(case_size)
        handle_case(case_line, data)
        case_line += 1    

def read_case(case_size):
    for case_line in range (1, case_size):
        stuff = input().split()
        points = list().append(stuff)
        
    return 

def handle_case(case_line, data):
    if case_line == 1:
        print('Photo')
    print(data)
    #print('({}, {})'.format(x, y))

    
if __name__ == '__main__':
    main()