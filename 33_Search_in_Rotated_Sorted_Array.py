class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        def findDivision(lo, hi):
            if lo == hi:
                return lo
            if lo > hi:
                raise Exception("Error")
            if nums[lo] < nums[hi]:
                return lo
            # if nums[lo] >= nums[hi]:
            mid = int((lo+hi)/2)
            if nums[mid] > nums[hi]:
                return findDivision(mid+1, hi)
            elif nums[mid] < nums[hi]:
                return findDivision(lo, mid)
            else:
                return findDivision(mid+1, hi)


        divisionIndex = findDivision(0, len(nums)-1)

        # def searchIter(lo, hi):
        #     if lo < hi:
        #         return False
        #     if lo == hi:
        #         return nums[lo] == target
        #     mid = int((lo+hi)/2)
        #     if nums[mid] == target:
        #         return True
        #     # mid in the left part
        #     if nums[mid] > nums[hi]:
        #         if nums[mid] > target:
        def binarySearch(lo, hi):
            if lo > hi:
                return None
            if lo == hi:
                if nums[lo] == target:
                    return lo
                else:
                    return None
            mid = (lo + hi) // 2
            if nums[mid] > target:
                return binarySearch(lo, mid-1)
            elif nums[mid] < target:
                return binarySearch(mid+1, hi)
            else:
                return mid

        low = divisionIndex - len(nums)
        result = binarySearch(low, divisionIndex-1)
        if result is None:
            return -1
        elif result < 0:
            return result + len(nums)
        else:
            return result

if __name__ == '__main__':
    s = Solution()
    print(s.search([5,1,3], 5))
