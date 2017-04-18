class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return string.join(word[::-1] for word in string.split(s))

"""
string.spilt(s[, sep[, maxspilt]]), return a list of the words of the string s
string.join(words[, sep]), concatenate a list or tuple of words with intervening occurrences of sep.
e.g. string.join(string.split(s, sep), sep) = s
"""
