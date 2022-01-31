'''
Problem Statement
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
'''

'''
"abbccbb"
k = 2
value = b
dict = {a:1, b:1, c:1}  count = 3 i.e. k = 0

for i in s:
  while i in s:
    a += 1
  while i not in s:
    



'''

#"aabccbb"


# class Solution():
#     def LongestSubstringSameLetters(self, s, k):
#         beg = 0
#         dict_val = {}
#         result = 0
#         temp = 0
#         for index, value in enumerate(s):
#             if value in dict_val:
#                 dict_val[value] += 1
#             elif value not in dict_val:
#                 dict_val[value] = 1
#             temp = max(temp, dict_val[value])
#             if index - beg + 1 - temp > k:
#                 dict_val[s[beg]] -= 1
#                 beg += 1
#
#             if index - beg + 1 > result:
#                 result = index - beg + 1
#         return result

class Solution():
    def LongestSubstringSameLetters(self, s, k):
        dict_fre = {}
        left, right, max_len = 0,0,0
        for right, value in enumerate(s):
            if value not in dict_fre:
                dict_fre[value] = 0
            dict_fre[value] += 1

            while len(dict_fre) > k+1:
                  dict_fre[left] -= 1
                  if dict_fre[left] == 0:
                      del dict_fre[left]
                  left += 1
            max_len = max(max_len, right - left + 1)
        return max_len








# class Solution():
#     def LongestSubstringSameLetters(self, str, k):
#         window_start, max_length, max_repeat_letter_count = 0, 0, 0
#         frequency_map = {}
#
#         # Try to extend the range [window_start, window_end]
#         for window_end in range(len(str)):
#             right_char = str[window_end]
#             if right_char not in frequency_map:
#                 frequency_map[right_char] = 0
#             frequency_map[right_char] += 1
#             max_repeat_letter_count = max(
#                 max_repeat_letter_count, frequency_map[right_char])
#
#             # Current window size is from window_start to window_end, overall we have a letter which is
#             # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
# #             # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.
# #             # if the remaining letters are more than 'k', it is the time to shrink the window as we
# #             # are not allowed to replace more than 'k' letters
#             if (window_end - window_start + 1 - max_repeat_letter_count) > k:
#                 left_char = str[window_start]
#                 frequency_map[left_char] -= 1
#                 window_start += 1
#
#             max_length = max(max_length, window_end - window_start + 1)
#         return max_length


def main():
    s = Solution()
    print(s.LongestSubstringSameLetters("abcabccbb", 2))
    # print(s.LongestSubstringSameLetters("abbcb", 1))
    # print(s.LongestSubstringSameLetters("abccde", 1))
    # print(s.LongestSubstringSameLetters("aaaaaaaaaaaaabc", 2))
    # print(s.LongestSubstringSameLetters("aaaaaabccbb", 2))
    # print(s.LongestSubstringSameLetters("a", 2))


main()

