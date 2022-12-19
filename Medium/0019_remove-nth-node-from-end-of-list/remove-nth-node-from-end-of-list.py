# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reference: https://leetcode.com/problems/remove-nth-node-from-end-of-list/solutions/1164542/js-python-java-c-easy-two-pointer-solution-w-explanation/
        slow = fast = head
        for _ in range(n):  # Make fast n nodes ahead slow
            fast = fast.next
        if not fast: return head.next  # n is the same as the length of the list
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next  # slow.next = fast will cause error when n = 1 and the length of the list is 2
        return head
