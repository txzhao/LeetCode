class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Given a string, find the length of the longest substring without repeating characters.
        # type s: str
        # rtype: int
        
        maxlen = 1
        start_idx = 0
        idx_dic = {}
        
        if length == 0:
            return 0

        for idx in range(len(s)):
            if s[idx] in idx_dic and idx_dic[s[idx]] >= start_idx:
                maxlen = max(maxlen, idx - start_idx)
                start_idx = idx_dic[s[idx]] + 1
                
            idx_dic[s[idx]] = idx
        return max(maxlen, idx - start_idx + 1)
        
        
