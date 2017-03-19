class Solution(object):
    def hammingDistance(self, x, y):
        # Given two integers x and y, calculate the Hamming distance.
        # The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
        # type x: int
        # type y: int
        # rtype: int
        
        # XOR relation -> delete '0' -> calculate string length
        return len((bin(x^y)[2:]).replace('0', ''))

    
