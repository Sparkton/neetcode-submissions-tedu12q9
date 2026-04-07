class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ls = []
        i = 0
        while i < n:
            ctr = 0
            j = i
            while j < n:
                if temperatures[i] < temperatures[j]:
                    ls.append(ctr)
                    break
                ctr+=1
                j+=1
            else: 
                ls.append(0) 
            i+=1
        return ls
