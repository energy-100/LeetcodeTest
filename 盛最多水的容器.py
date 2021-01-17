def maxArea(self, height: List[int]) -> int:
    length = len(height)
    startindex = 0
    endindex = length - 1
    maxvalue = 0
    while (startindex != endindex):
        tmpvalue = (endindex - startindex) * min(height[startindex], height[endindex])
        if tmpvalue > maxvalue:
            maxvalue = tmpvalue
        if (height[startindex] < height[endindex]):
            startindex += 1
        else:
            endindex -= 1
    return maxvalue

maxArea([1,8,6,2,5,4,8,3,7])
