class Solution(object):
    def isPalindrome(self, x):
        # Determine whether an integer is a palindrome.
        # type x: int
        # rtype: bool
        
        # initialize
        reverse_x = 0
        old_x = x
        
        # rule out negative
        if x < 0:
            return False
        
        # get the reverse of integer
        while x != 0:
            reverse_x = 10*reverse_x + x%10
            x /= 10
            
        return reverse_x == old_x
    
