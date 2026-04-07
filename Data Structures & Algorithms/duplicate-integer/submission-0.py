class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for i in nums:
            if i in dct:
                dct[i] += 1
            else:
                dct[i] = 1
        for i in dct.values():
            # print(i)
            if i >= 2:
                return True
        return False