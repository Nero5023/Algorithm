# -*- coding:utf-8 -*-

class Parenthesis:
    def chkParenthesis(self, A, n):
        # write code here
        stack = []
        for ch in A:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if len(stack) == 0:
                    return False
                stack.pop()
            else:
                return False
        return len(stack) == 0

if __name__ == '__main__':
    print Parenthesis().chkParenthesis("()(()()",7)