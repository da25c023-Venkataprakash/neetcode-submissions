from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining=0
        a = defaultdict()
        for i in range(len(nums)):
            
            if target-nums[i] in a:
                return [a[target-nums[i]], i]

            a[nums[i]]=i