# Author Ian W
# Project G 

def main():

    
    while True:
        num_times = 0
        case_size = int(input()) 
        for case_line in range (1, case_size + 1):
            data = read_case()
            handle_case(case_line, data)
    

def read_case():
    
    data = input().split()
    x = data[0]
    y = data[1]
    my_dict = {'x, y': data}
    return my_dict

def handle_case(case_line, data):
    if case_line == 1:
        print('Photo')
    print(data)
    #print('({}, {})'.format(x, y))

    
if __name__ == '__main__':
    main()