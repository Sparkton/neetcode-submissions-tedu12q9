class Solution:
    def isValid(self, s: str) -> bool:
        kv = {
            ']':'[',
            ')':'(',
            '}':'{'
        }
        ls = []
        for i in s:
            if i in kv.values():
                ls.append(i)
            else:
                if len(ls) == 0 or ls.pop() != kv[i]:
                    return False
        if len(ls) == 0:
            return True
        return False