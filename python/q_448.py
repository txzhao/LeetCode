class Solution(object):
    def findDisappearedNumbers(self, nums):
        # Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        # Find all the elements of [1, n] inclusive that do not appear in this array.
        # type nums: List[int]
        # rtype: List[int]
        
        numset = set(nums)
        losenums = []
        
        for i in range(len(nums)):
            # check if numset contain sequence numbers
            if i + 1 not in numset:
                losenums.append(i + 1)
        
        return losenums
    
