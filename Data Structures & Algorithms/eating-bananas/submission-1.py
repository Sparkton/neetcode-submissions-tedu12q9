class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    # piles = 1,4,3,2
    # h = 9
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            ctr = 0
            for p in piles:
                ctr += math.ceil(float(p) / k)
            if ctr <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res