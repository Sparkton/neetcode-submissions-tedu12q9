class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            diff = target - n # If target is -8 and n is -5, diff is -3
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i