class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ways = [0] * (n+1)
        ways[0] = 1
        if s[0] == "0":
            ways[1] = 0
        else:
            ways[1] = 1
        

        for i in range(2, n+1):
            if s[i-1] != "0":
                ways[i] += ways [i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                ways[i] += ways[i-2]
        return ways[n]

      
        