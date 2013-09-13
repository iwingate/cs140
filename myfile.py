num_cases = int(input())
for i in range(num_cases):
    case_size = int(input())
    case = []
    for j in range(case_size):
        print(j)
        line = list(input())
        print(line)
        case += [line] 
    print('Case {}'.format(i + 1))
    print(case)

#http://uva.onlinejudge.org/external/111/11160.html