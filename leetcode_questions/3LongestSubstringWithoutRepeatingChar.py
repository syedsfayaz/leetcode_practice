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
print(s.lengthOfLongestSubstring("aunbfn"))