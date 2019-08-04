# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution 1
        l, r = 1, n + 1
        while l < r:
            m = (l + r) /2
            ret = guess(m)
            if ret == 0:
                return m
            elif ret == 1:
                l = m + 1
            else:
                r = m
