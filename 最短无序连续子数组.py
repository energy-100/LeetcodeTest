class Solution:
    def findUnsortedSubarray(self, nums: list) -> int:
        length = len(nums)
        start = length
        end = 0
        indexs = set()

        for i in range(length - 1):
            if (nums[i] > nums[i + 1]):
                start = i
                break

        for i in range(length - 1, 0, -1):
            if (nums[i] < nums[i - 1]):
                end = i
                break
        res = (end - start) + 1
        return 0 if res < 0 else res

        # for i in range(length):
        #     index=length-1-i
        #     for j in range(length-1-i):
        #         if(nums[j]>nums[index]):
        #             index=j
        #     if index!=length-1-i:
        #         nums[index],nums[length-1-i] = nums[length-1-i],nums[index]
        #         indexs.add(index)
        #         indexs.add(length-1-i)

        # return 0 if len(indexs) ==0 else max(indexs) - min(indexs)+1

        # for i in range(length):
        #     for j in range(i,length-1):
        #         if (nums[j]>nums[j+1]):
        #             if(start>j):
        #                 start=j
        #             if(end<(j+1)):
        #                 end=j+1
        #             nums[j+1], nums[j] = nums[j], nums[j+1]
        # res=end-start+1
        # return 0 if res<0 else res

# print([i for i in range(1,-1,-1)])
a=Solution()
print(a.findUnsortedSubarray([2,1]))