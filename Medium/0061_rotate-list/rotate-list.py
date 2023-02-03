# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Reference: https://leetcode.com/problems/rotate-list/solutions/1838907/python-visual-easy-to-understand-o-n-time-o-1-space/
        if not head or not head.next: return head  # List with length of 0 or 1
        last, l = head, 1
        while last.next:  # Get the length of the list and the last node of the list
            last = last.next
            l += 1
        k %= l
        if not k: return head  # No rotation if k == 0
        last.next = head  # Make the list circular with last node pointing to first node
        for _ in range(l - k):  # Get the last node of the rotated list, which is (l - k - 1)th node
            last = last.next
        ans, last.next = last.next, None  # Disconnect and return new head
        return ans
