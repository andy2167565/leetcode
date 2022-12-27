# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#======== <Solution 1> ========#
        if not head or not head.next: return head  # head with length of 0 or 1
        prev, curr, ans = None, head, head.next
        while curr and curr.next:
            nxt = curr.next
            if prev: prev.next = nxt  # Connect result of previous pair to next pair
            curr.next, nxt.next = nxt.next, curr  # Swap current node with next node
            prev, curr = curr, curr.next  # Move on to next pair
        return ans

#======== <Solution 2> ========#
        dummy = ListNode(None, head)
        prev, curr = dummy, head
        while curr and curr.next:
            prev.next, curr.next, prev.next.next = curr.next, curr.next.next, curr
            prev, curr = curr, curr.next
        return dummy.next

#======== <Solution 3> ========#
        if head and head.next:
            next_head = head.next.next  # head of next pair
            head, head.next = head.next, head  # Swap current pair
            head.next.next = self.swapPairs(next_head)  # Connect current pair to next pair
        return head
