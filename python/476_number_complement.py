class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        l = num.bit_length()
        return num^(2**l-1)
        
"""
int.bit_length()
return the number of bits necessary to represent an integer in binary, excluding the sign and leading zeros.

**

"""