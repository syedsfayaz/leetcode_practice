'''
Problem Statement
Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
Example 1:
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.
Example 2:
Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.
'''
import numpy as np
#[-3, 0, 1, 2, -1, 1, -2]
'''boot strap'''
# class Solution():
#     def search_triplets(self, arr):
#         dictionary = {}
#         result = []
#         for i in range(len(arr)-1):
#             for j in range(i+1, len(arr)-1):
#                 for k in range(j+1,len(arr)-1):
#                     if arr[i] + arr[j] + arr[k] == 0:
#                         #result.append([i,j,k])
#                         temp_list = [arr[i], arr[j], arr[k]]
#                         result.append(temp_list)
#         return result

class Solution():
    def search_triplets(self, arr):
        arr.sort()
        result = []
        #return (arr)
        for index, value in enumerate(arr):
            if index > 0 and value == arr[index - 1]:
                continue
            left, right = index + 1, len(arr) - 1
            while left < right:
                temp_sum = arr[left] + arr[right] + value
                if  temp_sum > 0:
                    right -= 1
                elif temp_sum < 0:
                    left += 1
                else:
                  result.append([arr[left], arr[right], value])
                  left += 1
                  while arr[left] == arr[left - 1] and left < right:
                      left += 1
        return (result)







s = Solution()
print(s.search_triplets([-3, 0, 1, 2, -1, 1, -2]))
#print(s.search_triplets([0, 0, 0]))
#print(s.search_triplets([-5, 2, -1, -2, 3]))

