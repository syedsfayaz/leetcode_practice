class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        empty_dict = {}
        len_list = len(self.nums)
        if len(self.nums) == 0 or len(self.nums) == 1:
            return []

        for index, val in enumerate(self.nums):
            val1 = self.target - val
            if val1 in empty_dict:
                return [index, empty_dict[val1]]
            empty_dict[val] = index