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

class Solution():
    def longestSubstring(self,Input, K):
        beg, end, length, Longest_sub = 0, 0, len(Input), 1
        character_set = {}
        while end < length:
            if Input[end] not in character_set:
                character_set[Input[end]] = 1
                end += 1
            elif Input[end] in character_set:
                character_set[Input[end]] += 1
                end += 1

            while len(character_set) > K:
                character_set[Input[beg]] -= 1
                if character_set[Input[beg]] == 0:
                    del character_set[Input[beg]]
                beg += 1
            string_len = end - beg + 1
            string_len = max(string_len,end - beg + 1)
           # if Longest_sub < string_len: Longest_sub = string_len
        return string_len

s = Solution()
print(s.longestSubstring("auxoyz", 2))
print(s.longestSubstring("araaci", 1))
