class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in match:
                return [match[diff], i]
            else:
                match[num] = i
        return []