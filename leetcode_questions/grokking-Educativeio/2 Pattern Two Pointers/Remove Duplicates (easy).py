'''
Problem Statement
Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the duplicates in-place return the new length of the array.
Example 1:
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:
Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''

# class Solution():
#     def removeduplicates(self, input):
#         i = 0
#         j = 1
#         while i < len(input) - 1:
#             while j < len(input):
#                 if input[i] == input[j]:
#                     input.pop(j)
#                 else:
#                     j += 1
#             i += 1
#             j = i + 1
#         return len(input)

class Solution():
    def removeduplicates(self, input):
        i = 0
        while i < len(input) - 1:
            if input[i] != input[i+1]:
                i += 1
            else:
                input.pop(i+1)
        return len(input)


#Time Complexity = O(n) Space = O(1)
s= Solution()
print(s.removeduplicates([2, 3, 3, 3, 6, 9, 9]))
print(s.removeduplicates([2, 2, 2, 11]))
print(s.removeduplicates([2, 2, 2]))

print(s.removeduplicates([2, 3, 3, 3, 6, 2, 9, 3, 9]))



