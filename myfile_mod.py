num_cases = int(input())
print(num_cases)
for i in range(num_cases):
    case_size = input()
    print(case_size)
    case = []
    for i in range(len(case_size)):
        line = list(input())
        print(line)
        case += [line] 
        #print('Case {}'.format(i + 1))
        #print(case)

#http://uva.onlinejudge.org/external/111/11160.html

