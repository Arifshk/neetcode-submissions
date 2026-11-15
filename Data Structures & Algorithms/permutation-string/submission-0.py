class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        count = {}
        for ch in s1:
            count[ch] = count.get(ch, 0) + 1

        for i in range(n - m + 1):
            window = {}
            for ch in s2[i:i + m]:
                window[ch] = window.get(ch, 0) + 1
            if window == count:
                return True

        return False