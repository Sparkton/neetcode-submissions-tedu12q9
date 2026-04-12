class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        return list(count.keys())[0:k]