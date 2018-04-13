
# Twp characters


import itertools

def twoCharaters(s):
    s_list = list(s)
    combi = list(itertools.combinations(set(s_list), 2))
    max_length = 0
    for pair in combi:
        test_pair = [l for l in s_list if l in pair]
        alt_check = len([l for i,l in enumerate(test_pair) if l==test_pair[abs(i-1)]])
        if alt_check == 0:
            if len(test_pair) > max_length:
                max_length = len(test_pair)

    return max_length
