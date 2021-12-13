class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars1 = [ord(i) - ord('a') for i in s1]
        chars2 = [ord(i) - ord('a') for i in s2]

        window = [0] * 26   ## all letters in alpahbet list
        target = [0] * 26   ## all letters in alpahbet list

        for value in chars1:
            target[value] += 1

        beg = 0
        for index, value in enumerate(chars2):
            window[value] += 1

            if index >= len(s1):
                window[chars2[beg]] -= 1
                beg += 1

            if window == target:
                return True
        return False