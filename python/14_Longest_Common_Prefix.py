class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        else:
            return self.checkPrefix(strs[0], strs)

    def checkPrefix(self, pre, strs):
        for str in strs:
            if str.startswith(pre):
                continue
            else:
                pre = pre[:-1]
                pre = self.checkPrefix(pre, strs)
        return pre
    