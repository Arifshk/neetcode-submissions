class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 #sliding window so right pointer is at index 1 
        maxp = 0
        while r < len(prices):  # while our right p is < length of list
            if prices[l] < prices [r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else: 
                l = r
            r += 1
        return maxp