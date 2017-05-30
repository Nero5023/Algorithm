class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if k == 0:
            return
        part1 = nums[-k:]
        part2 = nums[:len(nums)-k]
        part1.extend(part2)
        nums[:] = part1
        print nums

if __name__ == '__main__':
    s = Solution()
    s.rotate([1,2],4)