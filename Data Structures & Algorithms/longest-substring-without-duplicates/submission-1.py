class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
            ## create pointer at l = 0, and r will run in range
       ## create a set called window or visited, this stores our current window. 
       ## while statement from r < len(s)
       ## if s[r] is in window remove s[l]
       ## return longest window tracked
        window = set()
        l = 0
        longest = 0

        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            else:
                if s[r] not in window:
                    window.add(s[r])
                    longest = max(longest, r - l + 1)
                
        return longest
