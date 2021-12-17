# class Solution:
#
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         self = 'x'
#         #self.s = s
#         longest_string = ''
#         string = ''
#         i = j = 0
#         # abcabcbb  baacab
#         for x in range(len(s)):
#             while s[x] in string:
#                 string.remove(i)
#             string = string + s[x]
#             if len(longest_string) < len(string):
#                 longest_string = string
#         return len(longest_string)
#
#
#
#
#
#
#         if len(longest_string) < len(s[i:j]):
#             longest_string = s[i:j]
#
#         return len(longest_string)
#         # charSet = set()
#         # l = res = 0
#         # for r in range(len(s)):
#         #     while s[r] in charSet:
#         #         charSet.remove(s[l])
#         #         l += 1
#         #     charSet.add(s[r])
#         #     res = max(res, r -l + 1)
#         # return res
#
# x = Solution.lengthOfLongestSubstring('x', 'badacab')
# print(x)

### abccab
 ##  acaaacb
#abcdecfab

#set = (a, b, c, d, e, c

s = 'dvdf'


# def unique(s):
#     distinct = set()
#     longest = 0
#     j = 0
#     for i in range(len(s)):
#         while s[i] in distinct:
#             distinct.remove(s[j])
#             j += 1
#         distinct.add(s[i])
#         longest = max(longest, len(distinct))
#     return(longest)
#
# print(unique(s))

s = "abcbc"
def unique(s):
    dicti = {}
    i = 0
    max_len = 0
    for x,y in enumerate(s):
        if y in dicti and dicti[y] >= i:
            i = dicti[y] + 1
            dicti[y] = x
        else:
            dicti[y] = x
            max_len = max(max_len, x - i + 1)
    return max_len
print(unique(s))

# def longestPalindrome(s: str) -> str:
#     if len(s) == 0:
#         return ""

#     sub_range = len(s)
#     while sub_range > 0:
#         i = 0
#         number_times = len(s) - sub_range + 1
#         while number_times >= i:
#             pal = s[i: sub_range + i]
#             if pal and pal == pal[::-1]:
#                 return pal
#             i += 1
#         sub_range -= 1
#
#
# print(longestPalindrome('eabcb'))