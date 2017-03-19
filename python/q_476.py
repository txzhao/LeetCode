class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        n = len(bin(num)[2:])
        ones = 2**n - 1

        return int(bin(num^ones), 2)
