class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        letters = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        result = []
        for word in words:
            w = set(word.lower())
            if w.issubset(letters[0]) or w.issubset(letters[1]) or w.issubset(letters[2]):
                result.append(word)
        return result
        
"""
s.issubset(t), s<=t, test whether every element in s is in t
"""