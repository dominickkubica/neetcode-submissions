class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) -1

        while L <= R:
            midpoint = (R + L) // 2
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] > target:
                R = midpoint - 1
            else:
                L = midpoint + 1
        return -1