class Solution(object):
    def searchInsert(self, nums, target):
        #
        # type nums: List[int]
        # type target: int
        # rtype: int
        
        for idx, value in enumerate(nums):
            if target <= value:
                return idx
            else:
                if idx >= len(nums) - 1:
                    return idx + 1
