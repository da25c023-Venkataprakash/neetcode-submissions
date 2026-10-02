class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = [1] * len(nums)
        pre = [1] * len(nums)
        prefix=1
        for i in range(len(nums)):
            pre[i]= prefix
            prefix = prefix*nums[i]
        postfix=1
        for i in range(len(nums)):
            post[len(nums)-1-i] = postfix
            postfix = postfix * nums[len(nums) -1-i]
        return [p * s for p, s in zip(pre, post)]