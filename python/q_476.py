class Solution(object):
    def findComplement(self, num):
        # Given a positive integer, output its complement number. 
        # The complement strategy is to flip the bits of its binary representation.
        # type num: int
        # rtype: int

        n = len(bin(num)[2:])
        ones = 2**n - 1

        return int(bin(num^ones), 2)
