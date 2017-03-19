class Solution(object):
    def countBits(self, num):
        # Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num,
        # calculate the number of 1's in their binary representation and return them as an array.
        # type num: int
        # rtype: List[int]
        
        bits = []
        for i in range(num + 1):
            bits.append(bin(i).count('1'))
    
        return bits
