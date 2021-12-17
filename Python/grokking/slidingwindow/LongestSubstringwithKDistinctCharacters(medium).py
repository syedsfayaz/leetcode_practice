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

def longest_substring(String, k):
    beg = end = 0
    distinct = 0
    longest_string = 0
    c = len(Input)
    dictionary = {}
    while end < c:
        if String[end] not in dictionary:
            dictionary[end] = 0
        dictionary[end] += 1

        while len(dictionary.items()) > k:
            dictionary[String[beg]] -= 1
            if dictionary[String[beg]] == 0:
                dictionary.pop(String[beg])
        if  longest_string < end - beg + 1:
            longest_string = end - beg + 1
    return longest_string

 print(longest_substring(String="araaci", K=1))
