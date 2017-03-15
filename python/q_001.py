class Solution(object):
    def twoSum(self, nums, target):
        # Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        # You may assume that each input would have exactly one solution, and you may not use the same element twice.       
        # type nums: List[int]
        # type target: int
        # rtype: List[int]

        # initialize
        diff = [target - x for x in nums]
        
        for i in range(len(nums)):
            try:
                ind = diff.index(nums[i])
                if i != ind:
                    return [i, ind]
            
            # throw exception if value is not found in the list
            except ValueError:
                continue
