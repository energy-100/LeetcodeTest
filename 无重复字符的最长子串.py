class Solution:

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

a=Solution()
print(a.lengthOfLongestSubstring('au'))
# print(a.lengthOfLongestSubstring('abcabcbb'))