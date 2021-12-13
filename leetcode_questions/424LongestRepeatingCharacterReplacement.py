class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        beg = 0
        dict_val = {}
        result = 0
        temp = 0
        for index, value in enumerate(s):
            if value in dict_val:
                dict_val[value] += 1
            elif value not in dict_val:
                dict_val[value] = 1
            temp = max(temp, dict_val[value])
            if index - beg + 1 - temp > k:
                dict_val[s[beg]] -= 1
                beg += 1

            if index - beg + 1 > result:
                result = index - beg + 1
        return result
