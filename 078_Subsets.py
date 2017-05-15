class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == []:
            return [[]]
        without1 = self.subsets(nums[1:])
        # print without1
        with1 = map(lambda x:add(x,nums[0]), without1)
        without1.extend(with1)
        return without1

def add(x, y):
    x = x[:]
    x.append(y)
    return x

if __name__ == '__main__':
    s = Solution()
    print s.subsets([1,2,3])