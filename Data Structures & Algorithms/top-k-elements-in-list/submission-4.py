class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = {}
        for num in nums:
            ctr[num] = 1 + ctr.get(num, 0)

        heap = []
        for num in ctr.keys():
            heapq.heappush(heap, (ctr[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res