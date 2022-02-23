'''Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val'''

nums = [1, 2, 3, 4]

for i in range(len(nums) - 1, -1 , -1):
    print(i)