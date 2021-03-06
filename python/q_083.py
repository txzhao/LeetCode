# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        # Given a sorted linked list, delete all duplicates such that each element appear only once.
        # type head: ListNode
        # rtype: ListNode
        
        pos = head
    
        while pos:
            # delete repetitive nodes iteratively
            while pos.next and pos.next.val == pos.val:
                pos.next = pos.next.next
            pos = pos.next
        return head
        
