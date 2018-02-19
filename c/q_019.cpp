/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // define two pointers with interval n to track the nth node from end 
    struct ListNode *first = head, *second = head;
    int count = 0;
    
    while (first != NULL) {
        first = first->next;
        if (count > n) second = second->next;
        count++;
    }

    if (count <= n) {
        head = head->next;
    } 
    else second->next = second->next->next;
    
    return head;
}