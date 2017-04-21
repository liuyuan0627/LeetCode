class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for findNum in findNums:
            index = nums.index(findNum)
            flag = 0
            for num in nums[index:]:
                if num > findNum:
                    result.append(num)
                    flag == 1
                    break;
            if flag == 0:
                result.append(-1)
        return result