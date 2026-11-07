class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        window = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+=1
            window.add(s[right])
            longest = max(longest, (right-left+1))
        return longest


    # left = 0, window = set(), longest = 0
# for each r:
#     while s[r] is already in window:
#         remove s[left] from window
#         move left forward
#     add s[r] to window
#     longest = bigger of longest and window length (r - left + 1)
# return longest

