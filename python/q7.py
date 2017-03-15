class Solution(object):
    def reverse(self, x):
        # Reverse digits of an integer.
        # function should return 0 when the reversed integer overflows.
        # type x: int
        # rtype: int
        
        # initialize
        sum = 0
        digit = []
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # get digits of the integer reversely
        while x/10 != 0:
            digit.append(x%10)
            x /= 10
        digit.append(x)
        
        # get the reverse integer
        for i in range(len(digit)):
            sum *= 10
            sum += digit[i]
        
        # check if integer overflows
        # need hard code the limit since numbers in python have no limit
        if abs(sum) > 0x7FFFFFFF: 
            sum = 0
            
        return sign*sum

    
