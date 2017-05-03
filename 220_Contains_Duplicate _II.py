class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        for i in range(0, len(nums)):
            for j in range(i+1, min(len(nums), i+k+1)):
                if abs(nums[i]-nums[j]) <= t:
                    return True
        return False