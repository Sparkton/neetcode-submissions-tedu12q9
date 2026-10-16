class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        bucket = {}
        for i, n in enumerate(nums):
            if n in bucket and abs(i - bucket[n]) <= k:
                return True
            
            bucket[n] = i
        return False