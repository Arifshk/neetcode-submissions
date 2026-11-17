class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10 

        mod = 10**9 + 7
        jump = [
            [4,6], [6,8], [7,9], [4,8], [3,9,0], [], [1,7,0], [2,6], [1,3], [2,4]
        ] # 0 to 9 moves

        dp = [1] * 10#how many ways to land on ith digit 

        for _ in range(n-1):
            next_dp = [0]*10
            for digit in range(10):
                for j in jump[digit]:
                    next_dp[j] = (next_dp[j] + dp[digit]) % mod 
            dp = next_dp
        
        return sum(dp) % mod