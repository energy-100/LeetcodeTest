# a=[1,2,3,4,5,6]
# b=[1,2,3,4,5,6]

# print((1,1) in zip(a,b))
#
# import numpy as np
# from collections import Counter
#
# data = np.array([1.1, 1.1, 1.1, 2, 3, 5, 4, 4, 4, 5])
#
# # 方法一
# # print('Counter(data)\n', Counter(data))  # 调用Counter函数
# # print("abc".find())
# l=list("abcgdaewaa")
# tmpDict=dict()
# for elem in l:
#     tmpDict[elem]
import re

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



