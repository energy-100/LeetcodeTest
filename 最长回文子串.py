
def longestPalindrome( s: str) -> str:
    length = len(s)
    maxlen = 1
    startindex = 0
    bp = [[False for j in range(length)] for i in range(length)]
    for i in range(length):
        bp[i][i] = True

    for i in range(1, length):
        for j in range(i):
            if (s[j] != s[i]):
                bp[j][i] = False
            else:
                if (i - j <= 2):
                    bp[j][i] = True
                else:
                    bp[j][i] = bp[j + 1][i - 1]
                if(bp[j][i]==True):
                    currentMaxLen = i - j + 1
                    if (currentMaxLen > maxlen):
                        maxlen = currentMaxLen
                        startindex = j

    return s[startindex:startindex+maxlen]

def longestPalindrome_test( s: str) -> str:
    length=len(s)
    maxlen=1
    startindex=0
    bp=[[False for j in range(length)] for i in range(length)]
    for i in range(length):
        bp[i][i]=True
    for i in range(length):
        for j in range(i):
            if(s[j]!=s[i]):
                bp[j][i]=False
            else:
                if(i-j<=2):
                    bp[j][i] = True
                else:
                    bp[j][i] = bp[j+1][i-1]

            if(bp[j][i]==True):
                tmpmaxlen=i-j+1
                if(tmpmaxlen>maxlen):
                    maxlen=tmpmaxlen
                    startindex=j

    return s[startindex:startindex+maxlen]

    
    

print(longestPalindrome("aacabdkacaa"))

