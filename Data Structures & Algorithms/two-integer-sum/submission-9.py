class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []
        # l,r = 0, len(nums)-1
        # while l < r:
        #     x = nums[l]+nums[r]
        #     if x == target:
        #         return [l,r]
        #     elif x < target:
        #         r-=1
        #     else:
        #         l+=1
        # return [l,r]