class Solution(object):
    def singleNumber(self, nums):
        # Given an array of numbers nums, in which exactly two elements appear only once 
        # and all the other elements appear exactly twice. Find the two elements that appear only once.
        # type nums: List[int]
        # rtype: List[int]
        
        ones = set()
        twos = set()
        
        for i in nums:
            if i not in ones:
                ones.add(i)
            else:
                twos.add(i)
        
        # complement set contains single number
        return list(ones - twos)
