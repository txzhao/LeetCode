class Solution(object):
    def findWords(self, words):
        # Given a List of words, return the words that can be typed 
        # using letters of alphabet on only one row's of American keyboard.
        # type words: List[str]
        # rtype: List[str]
        
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        chosen_w = []
        
        for word in words:
            low_w = set(word.lower()) 
            # check if all letters are subset of one of the three lines
            if low_w.issubset(line1) or low_w.issubset(line2) or low_w.issubset(line3):
                chosen_w.append(word)
        return chosen_w
    
