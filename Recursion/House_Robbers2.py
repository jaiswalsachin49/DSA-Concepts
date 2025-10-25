def hor(nums):
    prev_rob = max_rob = 0

    for i in nums:
        temp = max(max_rob,prev_rob + i)
        prev_rob = max_rob
        max_rob = temp
    return max_rob

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        else:
            return max(hor(nums[:-1]), hor(nums[1:]),nums[0])
