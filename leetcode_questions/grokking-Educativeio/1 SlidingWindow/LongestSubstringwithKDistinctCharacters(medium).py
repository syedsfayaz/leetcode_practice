'''
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.
Example 1:
Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:
Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:
Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
'''


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # "abcabcbb"
#         i = 0
#         longest_substring = 0
#         if len(s) == 1: return 1
#         while i < len(s):
#             # print(i)
#             unique = s[i]
#             count = 1
#             for j in range(i + 1, len(s)):
#                 if s[j] not in unique:
#                     unique = unique + s[j]
#                     count += 1
#                     # print(longest_substring)
#                 else:
#                     break
#
#             if count > longest_substring:
#                 longest_substring = count
#             i += 1
#         return longest_substring


'''
Time Complexity = n * n = O(n2)


Space Complexity = O(n)

'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        window = set()
        beg, end, ans, n = 0, 0, 0, len(s)

        while beg < n and end < n:

            if s[end] not in window:
                window.add(s[end])
                end += 1
                ans = max(ans, (end - beg))
            else:
                window.remove(s[beg])
                beg += 1
        return ans
s = Solution()
print(s.lengthOfLongestSubstring("auxoyz"))

"""
Time complexiy = O(n)
Space = O(n)
"""