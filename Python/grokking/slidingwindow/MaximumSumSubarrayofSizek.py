'''Problem Statement #
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

Input: [2, 1, 5, 1, 3, 2]
k=3
def max_sum(Input, k):
    i = 0
    j = 3
    count = 0
    while j < len(Input):
        Total = sum(Input[i:j])
        if Total > count:
            count = Total
        i += 1
        j += 1
    return count

print(max_sum([2, 1, 5, 1, 3, 2], k=3))



