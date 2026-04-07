class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        # stack = [1,2,3,4,5]
        # print(stack[-1])
        ls = sorted(list(zip(position, speed)), key=lambda x: x[0], reverse=True)
        for i, j in ls:
            ctr = (target-i)/j
            print(ctr)
            if not stack or ctr > stack[-1]:
                stack.append(ctr)
        
        return len(stack)