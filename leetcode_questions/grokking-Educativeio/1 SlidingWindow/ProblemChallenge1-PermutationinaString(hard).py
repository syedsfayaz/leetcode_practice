'''
Problem Challenge 1
Permutation in a String (hard)
Given a string and a pattern, find out if the string contains any permutation of the pattern.
Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:
abc
acb
bac
bca
cab
cba
If a string has ‘n’ distinct characters it will have n!n! permutations.
Example 1:
Input: String="oidbcaf", Pattern="abc"
Output: true
Explanation: The string contains "bca" which is a permutation of the given pattern.
Example 2:
Input: String="odicf", Pattern="dc"
Output: false
Explanation: No permutation of the pattern is present in the given string as a substring.
Example 3:
Input: String="bcdxabcdy", Pattern="bcdyabcdx"
Output: true
Explanation: Both the string and the pattern are a permutation of each other.
Example 4:
Input: String="aaacb", Pattern="abc"
Output: true
Explanation: The string contains "acb" which is a permutation of the given pattern.
'''

# class Solution():
#     def PermutationString(self, string, pattern):
#         st_dict = {}
#         pt_dict = {}
#         beg = 0
#         end = len(pattern)
#
#         for i in pattern:
#             if i not in pt_dict:
#                 pt_dict[i] = 0
#             pt_dict[i] += 1
#
#         while end <= len(string):
#
#             temp = list(string[beg:end])
#             for item, value in pt_dict.items():
#                 #print(value, item)
#                 if item not in temp: break
#                 temp.remove(item)
#             if len(temp) == 0:
#                 return True
#             beg += 1
#             end += 1
#         return False

# class Solution():
#     def PermutationString(self, str, pattern):
#         window_start, matched = 0, 0
#         char_frequency = {}
#
#         for chr in pattern:
#             if chr not in char_frequency:
#                 char_frequency[chr] = 0
#             char_frequency[chr] += 1
#
#
#         for index, value in enumerate(str):
#             #print(index, value)
#             if value in char_frequency:
#                 char_frequency[value] -= 1
#
#                 if char_frequency[value] == 0:
#                     matched += 1
#
#             if matched == len(char_frequency):
#                 return True
#
#             if index >= len(pattern) -1:
#
#                 if str[window_start] in char_frequency:
#                     if char_frequency[str[window_start]] == 0:
#                         matched -= 1
#                     char_frequency[str[window_start]] += 1
#                 window_start += 1
#         return False

class Solution():
    def PermutationString(self, str, pattern):
        char1_hash = [ord(i) - ord('a') for i in str]
        char2_hash = [ord(i) - ord('a') for i in pattern]

        target = [0] * 26
        window = [0] * 26

        for value in char2_hash:
            target[value] += 1

        beg = 0
        for index, value in enumerate(char1_hash):
            window[value] += 1

            if index >= len(pattern):
                window[char1_hash[beg]] -= 1
                beg += 1
            if window == target:
                return True
        return False



s = Solution()
print(s.PermutationString("oidbcaf", "abc"))
print(s.PermutationString("odicf", "dcf"))
print(s.PermutationString("aaacb", "abc"))
print(s.PermutationString("aaaaaacb", "aaacb"))
print(s.PermutationString("aca", "aac"))
print(s.PermutationString("eidboaoo", "ab"))

















