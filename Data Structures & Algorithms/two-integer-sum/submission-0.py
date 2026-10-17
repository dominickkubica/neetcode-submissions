class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match = {}
        for i, num in enumerate(nums):
            ans = target - num
            if ans in match:
                return [match[ans], i]
            match[num] = i