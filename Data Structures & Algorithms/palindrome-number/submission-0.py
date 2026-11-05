class Solution:
    def isPalindrome(self, x: int) -> bool:

        ## given int x
        ## return true if x is palindrome 
        ## return false otherwise 
        ## palindrome meaning same forward and back
        ## 111, 123
        ## brute force if iteration forward != backward return false but that gives two pases so O(n) Not optimal 
        ## optimal, is two pointers. One at 0 one at len(x) -1
        ## if string at left is equal to string at right, move both down end loop, otherwise return false


        s = str(x) ## converts int to string 
        l, r = 0, len(s) - 1

        while l < r: 
            if s[l] == s[r]:
                r -=1
                l += 1
            else: 
                return False
        return True
        
        

       
        
 


         
        