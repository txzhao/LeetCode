class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        diff = [target - x for x in nums]
        for i in range(len(nums)):
            try:
                ind = diff.index(nums[i])
                if i != ind:
                    return [i, ind]
            except ValueError:
                continue
