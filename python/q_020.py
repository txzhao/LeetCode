class Solution(object):
    def isValid(self, s):
        # Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        # The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
        # type s: str
        # rtype: bool
        
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
                
