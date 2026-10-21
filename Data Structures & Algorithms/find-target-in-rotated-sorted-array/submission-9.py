class Solution:
    def search(self, n: List[int], target: int) -> int:
        l, r = 0, len(n) - 1
        while l <= r:
            mid = l + (r - l)//2
            if n[mid] == target:
                return mid

            if n[l] <= n[mid]:
                if n[l] <= target < n[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if n[mid] < target <= n[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1