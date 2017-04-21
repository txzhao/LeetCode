class Solution(object):
    def permute(self, nums):
        # Given a collection of distinct numbers, return all possible permutations.
        # type nums: List[int]
        # rtype: List[List[int]]
        
        # itertools.permutations() returns tuples with all possible orderings, no repeated elements
        return map(list, itertools.permutations(nums))
