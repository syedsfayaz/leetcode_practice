'''
Problem Statement
Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
Example 1:
Input: [1, 2, 3, 4, 6], target=6
Output: [1, 3]
Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6
Example 2:
Input: [2, 5, 9, 11], target=11
Output: [0, 2]
Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
'''
from collections import defaultdict
class Solution():
    def pair_with_targetsum(self, arr, target_sum):
        values_dict = {}
        for index, values in enumerate(arr):
            diff = target_sum - values
            if diff not in values_dict:
                values_dict[values] = index
            else:
                return [values_dict[diff], index]

s = Solution()
print(s.pair_with_targetsum([2, 5, 9, 11], 11))