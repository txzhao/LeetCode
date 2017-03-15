class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reverse_x = 0
        old_x = x
        if x < 0:
            return False
        while x != 0:
            reverse_x = 10*reverse_x + x%10
            x /= 10
        return reverse_x == old_x
