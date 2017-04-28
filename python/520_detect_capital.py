class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return(word.islower() == True or word.isupper() == True or word.istitle() == True)
        
"""
str.islower(), All letters in this word are not capitals
str.isupper(), All letters in this word are capitals
str.istitle(), Only the first letter in this word is capital if it has more than one letter
"""