class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        fewest = [float("inf")] * (amount + 1)
        fewest[0] = 0
        if amount == 0:
            return 0

        for i in range(1, (amount+1)):
            for c in coins:
                if c <= i:
                    fewest[i] = min(fewest[i], fewest[i-c] + 1)
        if fewest[amount] == float("inf"):
            return -1
                
        return fewest[amount]
