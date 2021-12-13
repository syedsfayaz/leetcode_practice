'''
Problem Challenge 4
Words Concatenation (hard)
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.
Example 1:
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".
Example 2:
Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".
'''
from collections import defaultdict, Counter
#"catcatfoxfox", Words=["cat", "fox"]
target = {"cat": 1, "fox": 1}
window = {"cat": 0,"fox": 1 }
match = 1

class Solution():
    def findSubstring(self, s, words):
        target = Counter(words)
        window = defaultdict(int)
        len_allwords = 0
        for value in target:
            len_allwords += len(value)
        match = 0
        result = []
        beg = index = 0
        end = len(words[0])
        while end <= len(s):
            Word_char = s[beg:end]
            if Word_char in target:
               window[Word_char] += 1
               if window[Word_char] == target[Word_char]:
                   match += 1
            if match == len(target):
                result.append(index)
            if end - index + 1 >= len_allwords:
                window[s[index:index+len(words[0])]] -= 1
                if window[s[index:index+len(words[0])]] < target[s[index:index+len(words[0])]]:
                    match -= 1
                index += len(words[0])
            beg += len(words[0])
            end += len(words[0])
        return result

s = Solution()
# print(s.findSubstring("catfoxcat", ["cat", "fox"]))
# print(s.findSubstring("catcatfoxfox", ["cat", "fox"]))
# print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
# print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))



