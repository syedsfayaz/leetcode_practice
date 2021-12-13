class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
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
