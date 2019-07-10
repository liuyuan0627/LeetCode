class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while True:
            l = len(s)
            if '()' in s:
                s = s.replace('()', '')
            elif '[]' in s:
                s = s.replace('[]', '')
            elif '{}' in s:
                s = s.replace('{}', '')
            if l == len(s):
                break
        if len(s) == 0:
            return True
        else:
            return False
            