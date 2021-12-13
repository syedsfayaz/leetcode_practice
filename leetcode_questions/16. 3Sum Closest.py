class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[:3])
        for index, value in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            while left < right:
                temp_sum = value + nums[left] + nums[right]
                if abs(temp_sum - target) < abs(target - result):
                    result = temp_sum
                    # left += 1

                if temp_sum < target:
                    left += 1
                else:
                    right -= 1

        return (result)
