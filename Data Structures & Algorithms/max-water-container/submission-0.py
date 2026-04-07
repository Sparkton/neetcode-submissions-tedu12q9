class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        ctr = 0
        while left < right:
            x = min(heights[left], heights[right])*abs(left-right)
            if x > ctr:
                ctr = x
            if heights[left] > heights[right]:
                right-=1
            else:
                left+=1 
        return ctr