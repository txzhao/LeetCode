class Solution(object):
    def intToRoman(self, num):
        # Given an integer, convert it to a roman numeral.
        # Input is guaranteed to be within the range from 1 to 3999.
        # type num: int
        # rtype: str
        
        # define tuples which contain int and corresponding roman
        int_rom = [(1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'), (10, 'X'), (40, 'XL'), (50, 'L'), 
            (90, 'XC'), (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'), (1000, 'M')]
        rightpoint = len(int_rom) - 1
        romans = ''
        
        # transform the int into romans
        while num:
            if num >= int_rom[rightpoint][0]:
                romans += int_rom[rightpoint][1]
                num -= int_rom[rightpoint][0]
            else:
                rightpoint -= 1
        
        return romans
    
        # another simple way
        # M = ["", "M", "MM", "MMM"];
        # C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
        # X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
        # I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];
        # return M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10];
        
