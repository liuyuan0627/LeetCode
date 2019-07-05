class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            ret = - int(str(-x)[::-1])
        else:
            ret = int(str(x)[::-1])
        if (ret > 2**31 - 1) or (ret < -2**31):
            return 0
        else:
            return ret
