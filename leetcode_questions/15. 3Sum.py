class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        # return (arr)
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                temp_sum = nums[left] + nums[right] + value
                if temp_sum > 0:
                    right -= 1
                elif temp_sum < 0:
                    left += 1
                else:
                    result.append([nums[left], nums[right], value])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return (result)
