# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution 1
        
        l = 1
        r = n
        while l < r:
            m = l + (r - l) / 2
            if isBadVersion(m) is True:
                r = m
            else:
                l = m + 1
        return l
        
        # solution 2
    """
        return self.badVersion(1, n)
    
    def badVersion(self, start, end):
        index = (start + end) / 2
        if isBadVersion(index):
            if index == 1:
                return 1
            elif not isBadVersion(index-1):
                return index
            else:
                return self.badVersion(start, index-1)
        else:
            if isBadVersion(index + 1):
                return index + 1
            else:
                return self.badVersion(index + 1, end)
    """


"""
Find the fist index of True.
Binary Search
"""
