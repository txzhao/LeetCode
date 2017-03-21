class Solution(object):
    def detectCapitalUse(self, word):
        # Given a word, you need to judge whether the usage of capitals in it is right or not.
        # type word: str
        # rtype: bool
        
        return word.isupper() or word.islower() or word.istitle()
