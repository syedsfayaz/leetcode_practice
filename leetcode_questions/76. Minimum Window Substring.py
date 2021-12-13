from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = defaultdict(int)
        min_lenStr = s + t
        matched = 0

        beg = 0
        for index, value in enumerate(s):
            if value in target:
                window[value] += 1

                if window[value] == target[value]:
                    matched += 1

            while matched == len(target):
                temp = s[beg:index + 1]
                if len(min_lenStr) > len(temp):
                    min_lenStr = temp
                if s[beg] not in target:
                    window[s[beg]] -= 1
                    beg += 1
                elif s[beg] in target and window[s[beg]] > target[s[beg]]:
                    window[s[beg]] -= 1
                    beg += 1
                else:
                    break

        return min_lenStr if matched == len(target) else ""