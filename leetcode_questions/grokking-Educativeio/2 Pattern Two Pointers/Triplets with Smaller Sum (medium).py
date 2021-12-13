'''
Problem Statement
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
Example 1:
Input: [-1, 0, 2, 3], target=3
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Example 2:
Input: [-1, 4, 2, 1, 3], target=5
Output: 4
Explanation: There are four triplets whose sum is less than the target:
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
'''

class Solution():
    def triplet_sum_close_to_target(self, arr, target):
        arr.sort()
        result = sum(arr[:3])

        for index, value in enumerate(arr):
            left, right = index + 1, len(arr) -1

            while left < right:
                sumhere = value + arr[left] + arr[right]
                if sumhere < target and sumhere > result:
                    result = sumhere
                if sumhere < target:
                    left += 1
                else:
                    right -= 1
        return (result)


s = Solution()
print(s.triplet_sum_close_to_target([-1, 0, 2, 3], target=3))
print(s.triplet_sum_close_to_target([-1, 4, 2, 1, 3], target=5))
# # print(s.triplet_sum_close_to_target([1, 0, 1, 1], target=100))
# print(s.triplet_sum_close_to_target([-1,2,1,-4], target = 1))
# print(s.triplet_sum_close_to_target([0,1,2], target=0))