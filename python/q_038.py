class Solution(object):
    def countAndSay(self, n):
        # Given an integer n, generate the nth sequence: 1, 11, 21, 1211, 111221, ...
        # type n: int
        # rtype: str
        
        s = '1'
        
        for _ in range(n - 1):
            digit, temp, count = s[0], '', 0
            
            for d in s:
                # check if current digit equals the stored number
                # if so, count how many repetitive numbers
                if d == digit:
                    count += 1
                    
                # if not, stop counting and update temp, digit
                else:
                    temp += str(count) + digit
                    digit, count = d, 1
              
            temp += str(count) + digit
            s = temp
        
        return s
            
