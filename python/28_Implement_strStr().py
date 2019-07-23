class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.find(needle)
            #return haystack.index(needle)
        else:
            return -1
        
        
"""
a in b
string.find(obj)
string.index(obj)
"""
