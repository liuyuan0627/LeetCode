class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # solution 1
        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
            nums.append(0)
            
        # solution 2
        """
        zeros = 0
        i = 0
        while i != len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zeros += 1
            else:
                i += 1
        nums.extend([0] * zeros)
        """
 
 """
 list.count(obj)
 list.remove(obj)
 list.append(obj)
 list.pop(index)
 list.entend(list)
 """
