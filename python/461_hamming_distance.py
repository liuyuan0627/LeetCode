class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count("1")
        
"""
^ bitwise XOR
& bitwise AND
| bitwise OR
or    boolean OR
and   boolean AND
not x boolean NOT

bin(x)
convert an integer number to a binary string

str.count(sub[, start, end])
return the number of sub in the range [start, end]
"""