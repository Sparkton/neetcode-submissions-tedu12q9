class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        print("start")
        def bst(nums: List[int]) -> bool:
            l, r = 0 , len(nums) - 1
            while l <= r:
                print(nums[l:r])
                m = l + (( r - l) // 2)

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return True
            print("end2")
            return False

        print("mid")
        for i in matrix:
            if target >= i[0] and target <= i[-1]:
                print(i)
                return bst(i)
            print("end1")
        return False