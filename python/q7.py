class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sum = 0
        digit = []
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x/10 != 0:
            digit.append(x%10)
            x /= 10
        digit.append(x)
        for i in range(len(digit)):
            sum *= 10
            sum += digit[i]
        if abs(sum) > 0x7FFFFFFF: 
            sum = 0
        return sign*sum
