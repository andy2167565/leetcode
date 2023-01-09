# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/add-two-numbers/solutions/1016/clear-python-code-straight-forward/
        dummy = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, value = divmod(carry, 10)
            curr.next = ListNode(value)
            curr = curr.next
        return dummy.next

#======== <Solution 2> ========#
        def toint(node):
            return node.val + 10 * toint(node.next) if node else 0
        def tolist(n):
            q, r = divmod(n, 10)
            node = ListNode(r)
            if q:
                node.next = tolist(q)
            return node
        return tolist(toint(l1) + toint(l2))
