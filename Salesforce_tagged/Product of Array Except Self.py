'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
'''


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        if nums_len == 0: return None
        if nums_len == 1: return nums
        output = [1] * nums_len
        prefix = 1
        for index in range(len(nums)):
            output[index] = prefix
            prefix *= nums[index]
        postfix = 1
        for index in range(len(nums) - 1, -1, -1):
            output[index] *= postfix
            postfix *= nums[index]
        return output
