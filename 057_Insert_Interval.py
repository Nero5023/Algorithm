# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if intervals == []:
            return [newInterval]
        startIndex = binarySearch(intervals, 0, len(intervals)-1, newInterval)
        endIndex = binarySearchEnd(intervals, 0, len(intervals)-1, newInterval)
        print startIndex
        print endIndex
        newStart = min(intervals[startIndex].start, newInterval.start)
        newEnd   = max(intervals[endIndex].end, newInterval.end)
        if newInterval.end < intervals[endIndex].start:
            endIndex-=1
            newEnd = newInterval.end
        if newInterval.start > intervals[startIndex].end:
            startIndex+=1
            newStart = newInterval.start
        print startIndex
        print endIndex
        intervals[startIndex:endIndex+1] = [Interval(newStart, newEnd)]
        for x in intervals:
            print "[ ", x.start, ", " , x.end, "]"
        return intervals


# target : int
def binarySearch(intervals, start, end, newInterval):
    if start > end:
        return start
    mid = (start+end) / 2
    midInterver = intervals[mid]
    if midInterver.start == newInterval.start:
        return mid
    if midInterver.start > newInterval.start:
        return binarySearch(intervals, start, mid-1, newInterval)
    # midInterver.start < newInterval.start
    if mid == len(intervals)-1:
        return mid
    midNextInterver = intervals[mid+1]
    if midInterver.start < newInterval.start and newInterval.start <= midNextInterver.start:
        return mid
    return binarySearch(intervals, mid+1, end, newInterval)

def binarySearchEnd(intervals, start, end, newInterval):
    if start > end:
        return end
    mid = (start+end) / 2
    midInterver = intervals[mid]
    if midInterver.end == newInterval.end:
        return mid
    if midInterver.end < newInterval.end:
        return binarySearchEnd(intervals, mid+1, end, newInterval)
    # midInterver.end > newInterval.end 
    if mid == 0:
        return mid
    midBeforeInterver = intervals[mid-1]
    if midBeforeInterver.end < newInterval.end and newInterval.end < midInterver.end:
        return mid
    return binarySearchEnd(intervals, start, mid-1, newInterval)

if __name__ == '__main__':
    s = Solution()
    # ins = [Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)]
    # nIn = Interval(4,9)
    # s.insert(ins, nIn)
    # ins2 = [Interval(1,3), Interval(6,9)]
    # nIn2 = Interval(2,5)
    # s.insert(ins2, nIn2)
    s.insert([Interval(1,5)], Interval(6,8))