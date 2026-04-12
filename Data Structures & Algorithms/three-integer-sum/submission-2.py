class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # others = nums[:i] + nums[i+1:]
            others = nums[i+1:]
            # others.sort()
            l,r = 0, len(others) - 1
            while l < r:
                current_sum = others[l] + others[r] + nums[i]
                
                if current_sum > 0:
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    triplet = tuple(sorted((nums[i], others[l], others[r])))
                    res.append(triplet)
                    l += 1

        return list(set(res))