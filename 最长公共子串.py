
def demo(text1,text2):
    maxlen = 0
    len1 = len(text1)
    len2 = len(text2)
    if len1 > len2:
        minstr = text2
        maxstr = text1
    else:
        minstr = text1
        maxstr = text2

    for i in range(len(minstr), -1, -1):
        j1 = 0
        j2 = i
        while (j2 < len(minstr)):
            tmpstr = minstr[j1:j2+1]
            if tmpstr in maxstr:
                maxlen = max(maxlen, len(tmpstr))
            j1 += 1
            j2 += 1

    return maxlen

print(demo("abcde","erbcdet"))
