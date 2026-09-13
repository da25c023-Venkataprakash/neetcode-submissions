import random
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        while (2>0):
            x=random.randint(0,len(nums)-1)
            y=random.randint(0,len(nums)-1)
            if x<y:
                if nums[x]+nums[y] == target:
                    return [x,y]