class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ls = []
        for i in operations:
            try:
                if i.lstrip('-+').isdigit():
                    ls.append(int(i))
                elif i == 'C':
                    ls.pop(-1)
                elif i == 'D':
                    ls.append(2*ls[-1])
                else:
                    ls.append(ls[-1]+ls[-2])
            except:
                continue
            print(ls)
        return sum(ls)