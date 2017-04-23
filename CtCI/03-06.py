# -*- coding:utf-8 -*-
class TwoStacks:
    def twoStacksSort(self, numbers):
        # write code here
        stack = []
        while len(numbers) != 0:
            num = numbers.pop()
            while len(stack) != 0:
                if stack[-1] <= num:
                    break
                numbers.append(stack.pop())
            stack.append(num)
        stack.reverse()
        return stack

if __name__ == '__main__':
    print TwoStacks().twoStacksSort([1,6,3,4,2])