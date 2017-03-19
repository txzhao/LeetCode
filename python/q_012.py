class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        int_rom = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
        romans = ''
        rightpoint = 12
 
        while num != 0:
            if num >= int_rom[rightpoint][0]:
                romans += int_rom[rightpoint][1]
                num -= int_rom[rightpoint][0]
            else:
                rightpoint -= 1
        
        return romans
