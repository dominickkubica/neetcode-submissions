class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_seen = float('inf')
        max_profit = 0

        for price in prices:
            lowest_seen = min(lowest_seen,price)
            max_profit = max(max_profit, price - lowest_seen)
        return max_profit