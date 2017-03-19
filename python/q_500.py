class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        chosenwords = []
        
        for word in words:
            low_word = set(word.lower()) 
            if low_word.issubset(line1) or low_word.issubset(line2) or low_word.issubset(line3):
                chosenwords.append(word)
        return chosenwords
