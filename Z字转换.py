def convert(s: str, numRows: int) -> str:
    length = len(s)
    span = (numRows << 1) - 2
    res = ""
    for i in range(1, numRows - 1):
        index = i
        j = 0
        while (index < length):
            res += s[index]
            if (index + 2 * (numRows - 1 - i) < length):
                res += s[index + 2 * (numRows - 1 - i)]
            j += 1
            index = i + j * span
    index = 0
    tmpstr = ""
    j=0
    while (index < length):
        tmpstr += s[index]
        j += 1
        index = 0 + j * span

    res = tmpstr + res

    index = numRows - 1
    j=0
    while (index < length):
        res += s[index]
        j += 1
        index = numRows - 1 + j * span

    return res



def convert_slim(s: str, numRows: int) -> str:
    if (numRows == 1):
        return s
    length = len(s)
    span = (numRows - 1) * 2
    res = ""
    for i in range(0, numRows):
        j = 0
        index = i
        while (index < length):
            res += s[index]
            if (i != 0 and i != numRows - 1):
                index2 = index + ((numRows - 1 - i) * 2)
                if (index2 < length):
                    res += s[index2]
            j += 1
            index = j * span + i
    return res

# print(convert("PAYPALISHIRING",3))
print(convert_slim("PAYPALISHIRING",3))