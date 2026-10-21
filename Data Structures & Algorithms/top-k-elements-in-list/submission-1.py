import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        h = []
        result = []
        for num in nums:
            freq[num] +=1


        for num in freq:
            heapq.heappush(h, (freq[num],num))
            if len(h) > k:
                heapq.heappop(h)
        for pair in h:
            result.append(pair[1])
        return result