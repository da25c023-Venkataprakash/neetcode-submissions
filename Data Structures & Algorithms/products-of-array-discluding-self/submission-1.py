class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix= [1]*len(nums)
        postfix = [1] * len(nums)

       
     
        for i,n in enumerate(nums):
            if i!=0:
                prefix[i]=nums[i-1]*prefix[i-1]
        
       
        for i in range(len(nums)-1,-1,-1):
            if i!=len(nums)-1:
                postfix[i]=nums[i+1]*postfix[i+1]


        return([s*j for s,j in zip(prefix,postfix)])



        