class Solution(object):
    def romanToInt(self, s):
        # Given a roman numeral, convert it to an integer.
        # type s: str
        # rtype: int
        
        # initialize a dictionary
        romans = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        sum = 0
        
        # check if current roman character has smaller value than the right roman character
        # to decide the sign of the roman
        for i in range(len(s) - 1):
            if romans[s[i]] < romans[s[i + 1]]:
                sum -= romans[s[i]]
            else:
                sum += romans[s[i]]
                
        return sum + romans[s[-1]]
    
