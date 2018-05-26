import operator


def find_digital_number(N):
    """
    N is a nagetive number, find each digital number from 0 to N.
    """
    
    print(N)
    rv = dict()
    size = len(str(N))  # digital number of i
    while N > 0:
        size -= 1
        div, mod = divmod(N, pow(10, size))
        # print('{} | {}'.format(div, mod))

        if str(div) not in rv:
            rv[str(div)] = 1
        else:
            rv[str(div)] += 1

        if mod == 0:
            if '0' in rv:
                rv['0'] += size
            else:
                rv['0'] = size
            break

        N = mod

    x = sorted(rv.items(), key=operator.itemgetter(1))
    return x
        
print(find_digital_number(109))
print(find_digital_number(1090))
print(find_digital_number(19999))
