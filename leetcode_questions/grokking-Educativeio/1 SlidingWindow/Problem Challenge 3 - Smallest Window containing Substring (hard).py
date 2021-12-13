'''
Problem Challenge 3
Smallest Window containing Substring (hard)
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
Example 1:
Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
Example 2:
Input: String="abdabca", Pattern="abc"
Output: "abc"
Explanation: The smallest substring having all characters of the pattern is "abc".
Example 3:
Input: String="adcad", Pattern="abc"
Output: ""
Explanation: No substring in the given string has all characters of the pattern.
'''


from collections import  Counter

# class Solution():
#    def find_substring(self, str, pattern):
#        char_pattern = {}
#        for value in pattern:
#            if value not in char_pattern:
#                char_pattern[value] = 0
#            char_pattern[value] += 1
#
#        window = {}
#        length = str
#        beg = 0
#        for index, value in enumerate(str):
#            if value in char_pattern:
#                if value not in window:
#                    window[value] = 0
#                window[value] += 1
#
#            while index != beg:
#                if window == char_pattern:
#                    if len(length) > len(str[beg:index+1]):
#                        length = str[beg:index+1]
#                else:
#                   break
#                window[str[beg]] -= 1
#                beg += 1
#        return length

#"aabdec", "abc"
# class Solution():
#    def find_substring(self, str, pattern):
#        charstr = [ord(i) - ord('a') for i in str]
#        charpat = [ord(i) - ord('a') for i in pattern]
#
#        window = [0] * 26
#        target = [0] * 26
#
#        for value in charpat:
#            target[value] += 1
#
#        beg = 0
#        substrings = []
#        for index, value in enumerate(charstr):
#            if value in charpat:
#                window[value] += 1
#
#                while target == window:
#                    substrings.append(str[beg:index])
#                    window[charstr[beg]] -= 1
#                    beg += 1
#        return min(substrings)


''' This is the correct solution all the above are not working'''
from collections import defaultdict, Counter
class Solution():
   def find_substring(self, str, pattern):
       target = Counter(pattern)
       window = defaultdict(int)
       min_lenStr = str + pattern
       matched = 0

       beg = 0
       for index, value in enumerate(str):
           if value in target:
               window[value] += 1

               if window[value] == target[value]:
                   matched += 1

           while matched == len(target):
               temp = str[beg:index + 1]
               if len(min_lenStr) > len(temp):
                   min_lenStr = temp
               if str[beg] not in target:
                   window[str[beg]] -= 1
                   beg += 1
               elif str[beg] in target and window[str[beg]] > target[str[beg]]:
                   window[str[beg]] -= 1
                   beg += 1
               else:
                   break


       return min_lenStr if matched == len(target) else ""


s = Solution()
print(s.find_substring("ADOBECODEBANC", "ABC"))
print(s.find_substring("abdabca", "abc"))
print(s.find_substring("ab", "A"))
print(s.find_substring("aa", "aa"))