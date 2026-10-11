class Solution:
    def sortColors(self, n: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r, i = 0, len(n)-1, 0
        while i <= r:
            if n[i] == 2:
                n[r], n[i] = n[i], n[r]
                r -=1
                i -= 1
            elif n[i] == 0:
                n[l], n[i] = n[i], n[l]
                l += 1
            i+=1