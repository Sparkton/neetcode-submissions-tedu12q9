class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ls = []
        for i in operations:
            print(i)
            if i == "+":
                ls.append(ls[-1]+ls[-2])
            elif  i == "C":
                ls.pop()
            elif  i == "D":
                ls.append(2 * ls[-1])
            else:
                ls.append(int(i))
        return sum(ls)