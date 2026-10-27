class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globmax = nums[0]
        currmax = 0
        for num in nums:
            currmax = max(num, currmax + num)
            globmax = max(globmax, currmax)
        return globmax