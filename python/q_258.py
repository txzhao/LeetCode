class Solution(object):
    def addDigits(self, num):
        # Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
        # type num: int
        # rtype: int
        
        # check if sum of digits needs another sum operation of digits
        while num >= 10:
            temp = 0
            while num > 0:
                temp += num % 10
                num /= 10
            num = temp
        return num
