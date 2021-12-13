'''
Problem Statement
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]
0,1,9,
'''
# [-2, -1, 0, 2, 3]
#
# [4]
# class Solution():
#
#     def sortedSquare(self, input):
#         for index, value in enumerate(input):
#             input[index] = value**2
#         return self.Sort(input)
#
#     def Sort(self, input):
#         if len(input) <= 1:
#             return input
#         midpoint = len(input) // 2
#         leftlist = self.Sort(input[0:midpoint])
#         rightlist = self.Sort(input[midpoint:])
#         return(self.merge_sort(leftlist, rightlist))
#
#
#     def merge_sort(self, leftlist, rightlist):
#         i = j = 0
#         result = []
#         while i <= len(leftlist) - 1 and j <= len(rightlist) - 1:
#             if leftlist[i] >= rightlist[j]:
#                 result.append(rightlist[j])
#                 j += 1
#             elif leftlist[i] <= rightlist[j]:
#                 result.append((leftlist[i]))
#                 i += 1
#         #result = result + leftlist[:i] + rightlist[:j]
#         print(result)
#         return result + leftlist[i:] + rightlist[j:]


# class Solution():
#     def sortedSquare(self, arr):
#       n = len(arr)
#       squares = [0 for x in range(n)]
#       highestSquareIdx = n - 1
#       left, right = 0, n - 1
#       while left <= right:
#         leftSquare = arr[left] ** 2
#         rightSquare = arr[right] ** 2
#         if leftSquare > rightSquare:
#           squares[highestSquareIdx] = leftSquare
#           left += 1
#         else:
#           squares[highestSquareIdx] = rightSquare
#           right -= 1
#         highestSquareIdx -= 1
#
#       return squares
class Solution():
    def sortedSquare(self, arr):
        result_array = [0] * len(arr)
        left = 0
        right = len(arr) - 1
        index = right
        while left <= right:
            left_array = arr[left] ** 2
            right_array = arr[right] ** 2
            if left_array < right_array:
                result_array[index] = right_array
                right -= 1
            else:# right_array <= left_array:
                result_array[index] = left_array
                left += 1

            index -= 1
        return result_array



s = Solution()
print(s.sortedSquare([-2, -1, 0, 2, 3]))
print(s.sortedSquare([-3, -1, 0, 1, 2]))
print(s.sortedSquare([-3, -2, -2, -1, 0, 1, 2]))
