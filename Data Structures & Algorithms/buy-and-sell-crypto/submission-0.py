class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_min = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-prev_min)
            prev_min = min(prev_min, prices[i])
        return max_profit

        