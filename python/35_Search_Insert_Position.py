class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # solution 1
        
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)

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
                    
"""
xrange(stop)
xrange(start, stop[, step])
Similar with range(), but returns an xrange object instead of a list.
"""
