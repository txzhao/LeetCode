class Solution(object):
    def longestCommonPrefix(self, strs):
        # find the longest common prefix string amongst an array of strings.
        # type strs: List[str]
        # rtype: str
        
        if strs == []:
            return ""
        
        # change strs into a list consisting of: list of 1st character, list of 2nd character,...list of nth character
        letter_group = zip(*strs)
        
        for i in range(len(letter_group)):
            # use set to delete repetitive characters 
            # len > 1 means different ith characters in strings
            if len(set(letter_group[i])) > 1:
                return strs[0][:i]
        
        # if all pass, then return the minimal common part
        return min(strs)
