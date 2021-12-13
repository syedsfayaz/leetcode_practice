'''
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.
Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:
Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
'''

class Solution():
    def MaximumSumSubarray(self, input, k):
        beg, end, list_len, Sum = 0, k, len(input), 0
        if list_len < k:
            return 0
        while end <= list_len:
            #print(input[beg:end])
            temp = sum(input[beg:end])
            if temp > Sum:
                Sum = temp
            #if end < list_len -1:
            beg += 1
            end += 1
        return Sum
s = Solution()
print(s.MaximumSumSubarray([2, 1, 5, 1, 3, 2], 3)) # 9
print(s.MaximumSumSubarray([2, 3, 4, 1, 5], 2)) # 7
print(s.MaximumSumSubarray([3, 4, 5], 2)) # 9
print(s.MaximumSumSubarray([4], 1)) # 9



"""
Time Complexity == Since its just one while loop. 
O(n)

Space complexity is O(1)
"""