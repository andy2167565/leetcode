# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle node of the list
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # Reverse the second half
        prev, curr = None, slow
        while curr:
            prev, curr.next, curr = curr, prev, curr.next
        # Merge lists
        head1, head2 = head, prev
        while head2.next:
            head1.next, head1 = head2, head1.next
            head2.next, head2 = head1, head2.next
