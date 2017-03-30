# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if len(prices) == 0:
#             return 0
#         stack = []
#         maxP = 0
#         for price in prices:
#             if len(stack) == 0:
#                 stack.append(price)
#                 continue
#             if stack[-1] <= price:
#                 stack.append(price)
#                 continue
#             profit = stack[-1] - stack[0]
#             if profit > maxP:
#                 maxP = profit
#             while len(stack) != 0 and stack[-1] > price:
#                 stack.pop()
#             stack.append(price)
#         profit = stack[-1] - stack[0]
#         if profit > maxP:
#             maxP = profit
#         return maxP

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        stack = []
        maxP = 0
        for price in prices:
            while len(stack) != 0 and stack[-1] > price:
                stack.pop()
            stack.append(price)
            
            profit = stack[-1] - stack[0]
            if profit > maxP:
                maxP = profit

        return maxP