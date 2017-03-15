class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rx = 0
        ox = x
        if x < 0:
            return False
        while x != 0:
            rx = 10*rx + x%10
            x /= 10
        return rx == ox
