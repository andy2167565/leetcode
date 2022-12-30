# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reference: https://leetcode.com/problems/odd-even-linked-list/solutions/133345/with-detailed-explanation-python/
        if not head: return head
        odd = head
        even = even_head = head.next  # Keep where the even-node list starts
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = even_head
        return head
