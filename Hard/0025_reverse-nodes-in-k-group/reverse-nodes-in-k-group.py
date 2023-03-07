# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/reverse-nodes-in-k-group/solutions/11491/succinct-iterative-python-o-n-time-o-1-space/
        dummy = prev_tail = ListNode(0)  # prev_tail is the last node in previous k-group
        dummy.next = l = r = head  # There are k nodes in the range [l, r] to be reversed in each round
        while True:
            count = 0
            while r and count < k:  # Use r to locate the range
                r = r.next
                count += 1
            if count < k:  # Arrive at the end of list
                return dummy.next
            prev, curr = r, l
            for _ in range(k):
                curr.next, prev, curr = prev, curr, curr.next  # Standard reversing
            prev_tail.next, prev_tail, l = prev, l, r  # Connect two k-groups and proceed to next round

#======== <Solution 2> ========#
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k:
            return head
        node, curr = None, head
        for _ in range(k):
            curr.next, node, curr = node, curr, curr.next
        head.next = self.reverseKGroup(curr, k)  # After reversing, head is the tail of current k-group and curr is the next pointer in original linked list order
        return node  # Node points at the new head of linked list after reversing
