class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Given a string, find the length of the longest substring without repeating characters.
        # type s: str
        # rtype: int
        
        # initialize
        length = len(s)
        maxlen = 1
        start_idx = 0
        idx_dic = {}
        
        if length == 0:
            return 0

        for idx in range(length):
            # check if current character has appeared
            # if so, update max length and start point of the substring
            if s[idx] in idx_dic and idx_dic[s[idx]] >= start_idx:
                maxlen = max(maxlen, idx - start_idx)
                start_idx = idx_dic[s[idx]] + 1  
            
            # keep update index dictionary
            idx_dic[s[idx]] = idx
        
        # don't forget the case that no repeating characters ever in a string
        return max(maxlen, idx - start_idx + 1)
        
        
