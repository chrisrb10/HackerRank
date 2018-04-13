# The time in words

words = {  0:"zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: 'twenty',
            30: 'thirty'
            }

def m_to_words(m):
    if m>20:
        if m%10 != 0:
            return (words[m//10*10]+' '+words[m%10])
        else:
            return (words[m])
    else:
        return (words[m])

def timeInWords(h, m):
    if m == 0:
        return ("{} o' clock".format(words[h]))
    if m == 30:
        return ('half past {}'.format(words[h]))
    if m ==15:
        return ('quarter past {}'.format(words[h]))
    if m ==45:
        return ('quarter to {}'.format(words[h+1]))
    if m>30:
        m_words = m_to_words(60-m)
        if m<59:
            return ('{} minutes to {}'.format(m_words, words[h+1]))
        else:
            return ('{} minute to {}'.format(m_words, words[h+1]))
    if m<30:
        m_words = m_to_words(m)
        if m==1:
            return ('{} minute past {}'.format(m_words, words[h]))
        else:
            return ('{} minutes past {}'.format(m_words, words[h]))
