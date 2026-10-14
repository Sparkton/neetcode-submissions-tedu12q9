class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        i, j = 0, min(len(w1), len(w2))
        newStr = ""
        while i < j:
            newStr += (w1[i]+w2[i])
            i += 1
        return newStr + w1[i:] + w2[i:]