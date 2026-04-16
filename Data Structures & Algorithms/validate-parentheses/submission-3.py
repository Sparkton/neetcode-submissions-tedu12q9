class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        dct = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        for i in s:
            if i in dct:
                if ls and ls[-1] == dct[i]:
                    ls.pop()
                else:
                    return False
            else:
                ls.append(i)

        return True if not ls else False