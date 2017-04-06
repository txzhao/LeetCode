class Solution(object):
    def lengthOfLastWord(self, s):
        # Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
        # return the length of last word in the string. If the last word does not exist, return 0.
        # type s: str
        # rtype: int
        
        if s == "":
            return 0
        
        while s[-1:] == ' ':
            s = s[:-1]
        
        return len(s) - 1 - s.rfind(' ')
