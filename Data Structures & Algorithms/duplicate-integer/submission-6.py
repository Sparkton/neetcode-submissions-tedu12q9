class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        m = len(set(nums))
        return True if n !=m else False