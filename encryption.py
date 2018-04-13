## Encryption


import math

def encryption(s):
    s = ''.join(s.split())
    #print(s)
    rows = math.floor((len(s))**(1/2))
    columns = math.ceil((len(s))**(1/2))
    #print(rows, columns)
    ar = [list(s[0+i:columns+i]) for i in range(0, len(s), columns)]
    diff = len(ar[0]) - len(ar[-1])
    if diff != 0:
        ar[-1] = ar[-1] + ['_']*diff
    #print(ar)
    code = [''.join(e) for e in list(zip(*ar))]
    code = [w.strip('_') for w in code]

    retval = ' '.join(code)
    return retval
