class Solution(object):
    def isValid(self, s):
        # Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        # The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
        # type s: str
        # rtype: bool
        
        # initialize a dictionary with brackets included as keys and values
        # define a stack 'brackets'
        dict = {')':'(','}':'{',']':'['}
        brackets = []
        
        for char in s:
            # append left brackets into stack
            if char in dict.values():
                brackets.append(char)
            
            # check if first right bracket fits the last left one
            # right bracket always starts to appear after the last left one
            elif char in dict.keys():
                # check if the string starts with a right bracket
                # the last pushed-in left bracket will be popped up first as the rule of stack
                if brackets == [] or dict[char] != brackets.pop():
                    return False
            else:
                return False
            
        # if everything goes well, the stack will be empty in the end
        # since all the stored left brackets could find their fits
        return brackets == []
                
