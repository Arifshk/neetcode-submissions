class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ##given array of intergers nums 
        ##FINAL task > RETURN LENGTH 
        ##of LONGEST CONSEQUITVE SEQUENCE 
        ##CONSECUTIVE SEQUENECE = each element is >= 1
        ##DO NOT NEED TO BE IN THE BEGGINING 

  
        ## GO through each Number, check if prev =< 1 
        ## if it is, add it to the array, if it is not, remove it. 

        seen = set(nums)
        longest = 0
        for n in seen:
            if n - 1 in seen:
                continue
            length = 1 
            while n + length in seen:
                length += 1
            longest = max(longest, length)
        return longest


                
            




        
        