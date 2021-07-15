
class Solution:
    '''
    滑动窗口，固定左指针，逐渐增加右指针，复合条件更新长度，不符合移动左指针
    '''
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s :return 0
        res=1
        left=0
        for right in range(len(s)):
            while(len(set(s[left:right+1]))>2):
                left+=1
            res=max(res,right-left+1)
        return res


if __name__ == '__main__':
    s=Solution()
    print(s.lengthOfLongestSubstringTwoDistinct("eceba"))