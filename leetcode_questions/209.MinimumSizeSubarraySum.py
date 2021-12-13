class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        beg = end = 0
        length = len(nums)
        smallest_subarray = length + 1
        if length == 0: return 0
        # if nums[beg] >= s:
        #     return 1
        sum = nums[beg]
        while beg < length or end < length:
            if sum < s and end+1 < length:
                end += 1
                sum += nums[end]
            elif sum >= s and beg < length:
                temp_val = end - beg + 1
                if (temp_val) < smallest_subarray: smallest_subarray = temp_val
                sum -= nums[beg]
                beg += 1
            else:
                return smallest_subarray if smallest_subarray != length + 1 else 0