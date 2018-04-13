
# Weighted uniform strings


import string

alphabet = list(string.ascii_lowercase)
w = [i+1 for i in range(26)]
weights = dict(zip(alphabet,w))

def weightedUniformStrings(s, queries):
    scores = set()
    ctr=1
    for i in range(len(s)):
        score = weights[s[i]]
        if (i+1 != len(s) and s[i+1] == s[i]):
            ctr += 1
        else:
            ctr = 1
        scores.add(score*ctr)

    retval = ['Yes' if n in scores else 'No' for n in queries]
    return retval
