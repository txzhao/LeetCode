# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # You are given two non-empty linked lists representing two non-negative integers. 
        # The digits are stored in reverse order and each of their nodes contain a single digit. 
        # Add the two numbers and return it as a linked list.
        
        # type l1: ListNode
        # type l2: ListNode
        # rtype: ListNode
        
        # define root node of a linked list
        root = node = ListNode(0)
        sign = 0

        # aggregate through list nodes
        # don't forget the case that l1, l2 are null while sign exists
        while l1 or l2 or sign:
            val1 = val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            sum = val1 + val2 + sign
            
            # update sign value
            if sum >= 10:
                node.next = ListNode(sum - 10)
                sign = 1
            else:
                node.next = ListNode(sum)
                sign = 0
            node = node.next
        
        return root.next
