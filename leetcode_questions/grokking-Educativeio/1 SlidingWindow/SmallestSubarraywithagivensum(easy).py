'''
Problem Statement
Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.
Example 1:
Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
Example 2:
Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:
Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
'''

'''
process to follow

take beg and end pointers  and use sliding window technique. 
Slide end to right when the sum is less than the provided S. Continue this until you reach the end of list. 
Slide beg to right when the sum is more than or equal to S. And remove left index when you move "beg" to right. 
Once all the elements are complete you will get your answer.  

'''

class Solution(object):
    def SmallestSubarray(self, input, S):
        beg = end = 0
        length = len(input)
        smallest_subarray = length + 1
        if length == 0: return 0
        if input[beg] >= S:
            return 1
        sum = input[beg]
        while beg < length or end < length:
            if sum < S and end+1 < length:
                end += 1
                sum += input[end]
            elif sum >= S and beg < length:
                temp_val = end - beg + 1
                if (temp_val) < smallest_subarray: smallest_subarray = temp_val
                sum -= input[beg]
                beg += 1
            else:
                return smallest_subarray if smallest_subarray != length + 1 else 0


s = Solution()
#print(s.SmallestSubarray([2, 1, 5, 2, 3, 2], 7))
print(s.SmallestSubarray([2, 1, 5, 2, 8], S=7))
# print(s.SmallestSubarray([3, 4, 1, 1, 6], S=8))
# print(s.SmallestSubarray([1, 1, 1, 1, 1], S=8))
# print(s.SmallestSubarray([], S=8))
# print(s.SmallestSubarray([0, 0], S=8))
# print(s.SmallestSubarray([9], S=8))







