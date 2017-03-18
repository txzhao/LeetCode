class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        dict = {')':'(','}':'{',']':'['}
        brackets = []
        
        for char in s:
            if char in dict.values():
                brackets.append(char)
            elif char in dict.keys():
                if brackets == [] or dict[char] != brackets.pop():
                    return False
            else:
                return False
        
        return brackets == []
                
