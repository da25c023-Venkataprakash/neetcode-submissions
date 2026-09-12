class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.array= [0]*2*len(nums)
        for i in range(len(nums)):
            self.array[i]=nums[i]
            self.array[i+len(nums)]=nums[i]

        return self.array