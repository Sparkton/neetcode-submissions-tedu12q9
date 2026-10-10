class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ctr = defaultdict(int)
        res = mx = 0
        for num in nums:
            ctr[num] += 1
            if mx < ctr[num]:
                res = num
                mx = ctr[num]
        return res