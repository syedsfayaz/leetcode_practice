'''
Triplet Sum Close to Target (medium)
Problem Statement
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet.
If there are more than one such triplet, return the sum of the triplet with the smallest sum.
Example 1:
Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:
Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
'''
'''Brut force'''
# class Solution():
#     def search_triplets(self, arr, target):
#         dictionary = {}
#         result = []
#         for i in range(len(arr)-2):
#             for j in range(i+1, len(arr)-1):
#                 for k in range(j+1,len(arr)):
#                     temp_sum = arr[i]+arr[j]+arr[k]
#                     if temp_sum <= target:
#                         result.append(temp_sum)
#         return max(result)


class Solution():
    def triplet_sum_close_to_target(self, arr, target):
        arr.sort()
        result = sum(arr[:3])

        for index, value in enumerate(arr):
            left, right = index + 1, len(arr) -1

            while left < right:
                sumhere = value + arr[left] + arr[right]
                if abs(sumhere - target) < abs(result - target):
                    result = sumhere
                if sumhere < target:
                    left += 1
                else:
                    right -= 1
        return (result)

'''Time Complexity = O(n2)
Space Complexity = O(1)'''
s = Solution()
# print(s.triplet_sum_close_to_target([-2, 0, 1, 2], target=2))
# print(s.triplet_sum_close_to_target([-3, -1, 1, 2], target=1))
# print(s.triplet_sum_close_to_target([1, 0, 1, 1], target=100))
print(s.triplet_sum_close_to_target([-1,2,1,-4], target = 1))
print(s.triplet_sum_close_to_target([0,1,2], target=0))