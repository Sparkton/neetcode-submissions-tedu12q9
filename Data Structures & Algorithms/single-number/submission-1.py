class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ls = []
        for x in nums:
            if x in ls:
                ls.remove(x)
            else:
                ls.append(x)

        # if ls:
        return ls[0]