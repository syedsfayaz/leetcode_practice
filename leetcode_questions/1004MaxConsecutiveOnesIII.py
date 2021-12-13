class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        beg = 0
        count = 0
        result = 0
        for index, val in enumerate(A):
            if val == 0:
                count += 1

            while count > K:
                if A[beg] == 0:
                    count -= 1
                beg += 1

            if index - beg + 1 > result:
                result = index - beg + 1
        return result