
#array manipulation

from itertools import accumulate
from collections import defaultdict

def arrayManipulation(n, queries):
    ar = defaultdict(int)
    for q in queries:
        #print(q)
        a, b, k = q
        ar[a] += k
        ar[b + 1] -= k
        #print(ar)
        #print(sorted(ar))
        #print([ar[i] for i in sorted(ar)])
        #print([e for e in accumulate([ar[i] for i in sorted(ar)])])
        #print(max(accumulate(ar[i] for i in sorted(ar))))
    return(max(accumulate(ar[i] for i in sorted(ar))))
