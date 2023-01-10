# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:  # Find the middle node of the list
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None  # Split the list into two smaller lists
        return self.merge(self.sortList(head), self.sortList(mid))  # Sort both lists and then merge them together

    def merge(self, l, r):
        if l.val > r.val: l, r = r, l  # Make sure l is the smaller node
        root = prev = l  # Use prev to keep track of the latest appended node
        l = l.next
        while l and r:
            if l.val < r.val:
                prev.next, l = l, l.next
            else:
                prev.next, r = r, r.next
            prev = prev.next
        prev.next = l or r
        return root
