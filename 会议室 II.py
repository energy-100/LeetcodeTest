class Solution:
    def minMeetingRooms(self, intervals) -> int:
        timelist = [(elem[0], 1) for elem in intervals] + [(elem[1], -1) for elem in intervals]
        timelist.sort()

        maxroom = 0
        currentroom = 0
        for elem in timelist:
            currentroom += elem[1]
            maxroom = max(maxroom, currentroom)

        return maxroom

#力扣版本
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        timelist = [(elem[0], 1) for elem in intervals] + [(elem[1], -1) for elem in intervals]
        timelist.sort()

        maxroom = 0
        currentroom = 0
        for elem in timelist:
            currentroom += elem[1]
            maxroom = max(maxroom, currentroom)

        return maxroom

if __name__ == '__main__':
    s=Solution()
    print(s.minMeetingRooms([[0,30],[5,10],[15,20]]))