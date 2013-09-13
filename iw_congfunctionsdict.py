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
    points = list()
    my_dict = {}
    for case_line in range(1, case_size + 1):
        stuff = input()
        points.append(stuff)
    my_dict['case size']  = case_size
    my_dict['points'] = points  
    return my_dict

def handle_case(case_line, data):
    print(data)
    

    
if __name__ == '__main__':
    main()