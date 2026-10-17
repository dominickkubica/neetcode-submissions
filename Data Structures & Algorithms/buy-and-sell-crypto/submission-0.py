class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_seen = float('inf')
        maxprofit = 0
        for price in prices:
            lowest_seen = min(lowest_seen, price)
            maxprofit = max(maxprofit, price - lowest_seen)
        return maxprofit