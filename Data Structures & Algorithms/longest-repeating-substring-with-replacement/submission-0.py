class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # IDEA: keep the most common letter, replace the rest.
        # Window is valid if (window size - most common count) <= k

        l = 0            # left edge of window
        count = {}       # letter -> how many times it's in the window (dict, NOT set: need HOW MANY)
        longest = 0      # best (record) window size so far

        for r in range(len(s)):        # r = index 0,1,2... (need index for r - l + 1)

            # new letter enters → +1 to its count
            # .get(x, 0) = "its count, or 0 if never seen" (no crash)
            count[s[r]] = count.get(s[r], 0) + 1

            # r - l + 1        = window size (+1 because both ends count, like pages 10-12 = 3)
            # max(count.values()) = most common letter's count (.values() = just the numbers)
            # size - most common  = letters I'd have to replace
            # > k = too many replacements → window broken
            # WHILE not if: may need to kick out more than one letter
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1       # leftmost letter leaves → its count goes down
                l += 1                 # window now starts one later

            # window is valid now → beat the record? save it (like a high score)
            longest = max(longest, r - l + 1)

        return longest

# TIME: O(n). r moves n times, l only moves FORWARD so max n times TOTAL → 2n.
#       NOT n² because l never resets.
#       max(count.values()) is O(1): at most 26 uppercase letters.
# SPACE: O(1). count holds at most 26 letters, no matter how long s is.







