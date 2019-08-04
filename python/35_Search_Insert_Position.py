class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # solution 1
        """
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)
        """
        """
        # solution 2
        if target in nums:
            return nums.index(target)
        else:
            for i in xrange(len(nums)):
                if nums[i] > target:
                    return i
            return i + 1
        """
        # solution 3
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) / 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        if nums[l] >= target:
            return l
        else:
            return l + 1

                    
"""
xrange(stop)
xrange(start, stop[, step])
Similar with range(), but returns an xrange object instead of a list.
"""
