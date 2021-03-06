'''
Problem Statement
Given a string, find the length of the longest substring which has no repeating characters.
Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
'''


class Solution():
    def NoRepeatingSubString(self, s):
        unique = set()
        #unique.add(s[0])
        final = 0
        beg, end = 0, 0

        # for index, value in enumerate(s):
        #         #         #     if value not in unique:
        #         #         #         unique.add(value)
        #         #         #     else:
        #         #         #         while value in unique:
        #         #         #             unique.remove(s[beg])
        #         #         #             beg += 1
        #         #         #         unique.add(value)
        #         #         #     length = index - beg + 1
        #         #         #     if length > final:
        #         #         #         final = length
        #         #         # return final
        if len(s) == 1: return 1
        while end < len(s) - 1 and beg < len(s):
            if end < len(s) -1 and s[end] not in unique:
                unique.add(s[end])
                temp = end - beg + 1
                final = max(final, temp)
                end += 1
            else:
                while s[end] in unique and beg < len(s) - 1:
                    unique.remove(s[beg])
                    beg += 1
        return final




s = Solution()
print(s.NoRepeatingSubString("aabccbb"))
print(s.NoRepeatingSubString("a"))
print(s.NoRepeatingSubString("aaabadbeccbb"))
print(s.NoRepeatingSubString(""))


