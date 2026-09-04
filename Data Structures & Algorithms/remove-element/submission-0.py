class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        j=0
        for i in range(len(nums)):
            i=i-j
            if nums[i]==val:
                nums.pop(i)
                j=j+1
                
                
            
            k= len(nums)

        return k
        