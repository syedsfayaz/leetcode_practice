'''
Problem Challenge 2
String Anagrams (hard)
Given a string and a pattern, find all anagrams of the pattern in the given string.
Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.
Example 1:
Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:
Input: String="abbcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".
'''

class solution():
    def find_string_anagrams(self, s, p):
        chars1 = [ord(i) - ord('a') for i in s]
        chars2 = [ord(i) - ord('a') for i in p]
        target = [0] * 26
        window = [0] * 26
        result = []
        for value in chars2:
            target[value] += 1
        beg = 0
        for index, value in enumerate(chars1):
            window[value] += 1

            if index >= len(p):
                window[chars1[beg]] -= 1
                beg += 1
            if window == target:
                result.append(beg)
        return result

''' using counter '''
# from collections import Counter
# class solution():
#     def find_string_anagrams(self, s, p):
#         if len(s) == 0:
#             return []
#         result = []
#         beg = 0
#         for index in range(len(s) - 1):
#             if index+len(p):
#                 window = s[index:index+len(p)]
#                 if self.compare_char(window, p):
#                     result.append(index)
#             else:
#                 break
#         return result
#
#     def compare_char(self, a, b):
#         if Counter(a) == Counter(b):
#             return True
#         return False


s = solution()
print(s.find_string_anagrams("ppqp", "pq")) ## 4 - 2 + 1 = 1
print(s.find_string_anagrams("abbcabc", "abc")) # 7 - 4 = 3




























