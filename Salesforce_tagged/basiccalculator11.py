'''
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
'''


class Solution:
    def calculate(self, s: str) -> int:

        '''multiplication, division
        division,
        addition,substraction.
'''
        stack = []
        operator = "+"
        ## "3+2*2+3"
        nums = 0

        for index in range(len(s)):
            # if s[index] == " ":
            #     continue
            # char = s[index]
            if s[index].isdigit():
                # print(s[index])
                nums = nums * 10 + int(s[index])
                # stack.append(nums)
            if s[index] != " " and not s[index].isdigit() or index == len(s) - 1:
                if operator == "+":
                    stack.append(nums)
                elif operator == "-":
                    stack.append(-nums)
                elif operator == "*":
                    stack[-1] *= nums
                elif operator == "/":
                    stack[-1] = int(stack[-1] / nums)

                nums = 0
                operator = s[index]
        print(stack)
        return sum(stack)












