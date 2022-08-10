# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#======== <Iterative Solution> ========#
        current = head
        # Loop through each type of digits -> 1, 2, 3, etc.
        while current:
            # Search identical digits
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        return head
        
#======== <Recursive Solution> ========#
        if head and head.next:
            if head.val == head.next.val:
                # Remove head.next and delete duplicates for head again
                head.next = head.next.next
                head = self.deleteDuplicates(head)
            else:
                # Delete duplicates for head.next
                head.next = self.deleteDuplicates(head.next)
        return head
