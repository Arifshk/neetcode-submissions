class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can = [False] * (len(s)+1)
        can[0] = True 

        for i in range(len(can)):
            for w in wordDict:
                if w == (s[i-len(w):i]) and can[i-len(w)] is True:
                    can[i] = True 
        return can[len(s)] 



        

        
        