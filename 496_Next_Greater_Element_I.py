class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """

        stack = []
        dic = {}
        for n in nums:
            while stack != [] and stack[-1] < n:
                dic[stack.pop()] = n
            stack.append(n)
        return [dic.get(n, -1) for n in findNums]