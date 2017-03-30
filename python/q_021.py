# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # Merge two sorted linked lists and return it as a new list. 
        # The new list should be made by splicing together the nodes of the first two lists.
        # type l1: ListNode
        # type l2: ListNode
        # rtype: ListNode
        
        # define a linked list
        root = node = ListNode(0)
        
        while l1 or l2:
            if not l1:
                node.next = l2
                return root.next
            if not l2:
                node.next = l1
                return root.next
            if l1.val <= l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next
            node = node.next
