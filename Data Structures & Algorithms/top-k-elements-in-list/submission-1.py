class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ls = []
        ls1 = []
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for val, cnt in count.items():
            ls.append([cnt, val])
        ls.sort()
        n = len(ls)
        while n > 0 and k > 0:
            ls1.append(ls.pop()[1])
            n -= 1
            k -= 1
        return ls1