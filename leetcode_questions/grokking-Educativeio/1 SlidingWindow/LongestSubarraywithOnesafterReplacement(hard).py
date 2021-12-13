'''
Problem Statement
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
Example 1:
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
'''

class Solution():
    def LongestSubarrayWithReplacement(self, s, k):
        beg = end = 0
        count = 0
        result = 0
        for index, val in enumerate(s):
            if val == 0:
                count += 1

            while count > k:
                if s[beg] == 0:
                    count -= 1
                beg += 1

            if index - beg + 1 > result:
                result = index - beg + 1
        return result



s = Solution()
print(s.LongestSubarrayWithReplacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2))
print(s.LongestSubarrayWithReplacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3))
print(s.LongestSubarrayWithReplacement([0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1], k=2))
print(s.LongestSubarrayWithReplacement([0, 0], k=2))





