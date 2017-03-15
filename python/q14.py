class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        letter_group = zip(*strs)
        for i in range(len(letter_group)):
            if len(set(letter_group[i])) > 1:
                return strs[0][:i]
        return min(strs)
