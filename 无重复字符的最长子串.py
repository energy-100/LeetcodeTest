class Solution:
    def lengthOfLongestSubstring_demo(self, s: str) -> int:
        length=len(s)
        if(length==0):
            return 0
        maxlength=1
        strtmplist=[s[0]]
        i=1
        while(i<length):
            if(s[i] not in strtmplist):
                strtmplist.append(s[i])
                maxlength=max(len(strtmplist),maxlength)
            else:
                strtmplist=strtmplist[strtmplist.index(s[i])+1:i]
                strtmplist.append(s[i])
            i += 1
        return maxlength





    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     length=len(s)
    #     slist=[]
    #     slist.append(s[0])
    #     maxlen=0
    #     i=0
    #     while i < length:
    #         j=i+1
    #         while j < length:
    #             if s[j] not in slist:
    #                 slist.append(s[j])
    #                 # j += 1
    #             else:
    #                 maxlen = max(maxlen, len(slist))
    #                 i = i+slist.index(s[j])+1
    #                 slist=slist[slist.index(s[j])+1:]
    #                 slist.append(s[j])
    #             j+=1
    #             if j==length :
    #                 break
    #
    #     return maxlen


    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length
        slist = []
        slist.append(s[0])
        maxlen = 0
        i = 0
        j = 1
        while j < length:
            if s[j] not in slist:
                slist.append(s[j])
                maxlen = max(maxlen, len(slist))
                # j += 1
            else:
                maxlen = max(maxlen, len(slist))
                i = i + slist.index(s[j]) + 1
                slist = slist[slist.index(s[j]) + 1:]
                slist.append(s[j])
            j += 1
            if j == length:
                break

        return maxlen

a=Solution()
# print(a.lengthOfLongestSubstring('au'))
print(a.lengthOfLongestSubstring_demo('aab'))
# print(a.lengthOfLongestSubstring('abcabcbb'))