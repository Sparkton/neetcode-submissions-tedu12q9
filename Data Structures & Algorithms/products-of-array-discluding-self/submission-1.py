class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        ctr = 1
        for i in range(len(nums)):
            res[i] = ctr
            ctr *= nums[i]
        ctr = 1
        for i in range(len(nums)-1 ,-1, -1):
            res[i] *= ctr
            ctr *= nums[i]
        return res