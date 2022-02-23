'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''





class Solution:
    def maxSubArray(self, nums):

        #         i, j = 0, 1
        #         temp_sum = sum = nums[i]
        #         nums_len = len(nums)

        #         if nums_len == 0: return None
        #         if nums_len == 1: return nums[0]
        #         while i < nums_len and j < nums_len:
        #               temp_sum += nums[j]
        #               if temp_sum > sum:
        #                    j += 1
        #               elif temp_sum < 0:
        #                   # temp_sum -= nums[i]
        #                   i = j
        #                   j += 1
        #                   temp_sum = 0
        #               sum = max(sum, temp_sum)
        # return(sum)
        prev = nums[0]
        curr = 0
        maxSum = prev
        for i in nums:
            if curr < 0:
                curr = 0
            curr += i
            maxSum = max(curr, maxSum)
        return maxSum

s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(s.maxSubArray([-2,-1,-3,-4,-1,-2,-1,-5,-4]))