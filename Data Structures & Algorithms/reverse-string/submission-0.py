class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, n = 0, len(s)
        while i < n/2:
            s[i], s[n-1-i] = s[n-1-i], s[i]
            print(s)
            i+=1