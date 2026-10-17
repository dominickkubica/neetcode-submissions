class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = defaultdict(list)
        for i, v in enumerate(nums):
            if v in seen:
                if abs(seen[v][-1] - i) <= k:
                    return True
            seen[v].append(i)
        return False