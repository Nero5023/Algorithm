import sys
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        for num in nums:
            print stack
            if len(stack) == 0 or num <= stack[-1][0]:
                stack.append((num, num))
            elif num < stack[-1][1]:
                return True
            else: # stack[-1][1] >= num
                last = stack.pop()
                last = (last[0], num)
                while len(stack) != 0 and num >= stack[-1][1]:
                    stack.pop()
                if len(stack) != 0 and num > stack[-1][0]:
                    return True
                stack.append(last)
        return False

if __name__ == '__main__':
    s = Solution()
    print s.find132pattern([-2,1,-2])
                    

