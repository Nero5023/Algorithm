class Solution(object):
    def findDuplicate(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            j = nums[i]
            if nums[i] == nums[j]:
                print j
                print nums
                return
            exchange(nums, i, j)
            print nums




def exchange(nums, i, j):
    nums[i] = nums[i] + nums[j]
    nums[j] = nums[i] - nums[j]
    nums[i] = nums[i] - nums[j]

if __name__ == '__main__':
    s = Solution()
    s.findDuplicate([2, 1, 3, 5, 4])