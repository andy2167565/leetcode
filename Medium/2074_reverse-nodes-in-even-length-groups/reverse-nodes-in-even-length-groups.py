# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, group_size = head, 2  # head won't be reversed whatsoever so start with length 2
        while prev.next:
            node, n = prev, 0
            for _ in range(group_size):  # Get actual group size
                if not node.next:
                    break
                n += 1
                node = node.next
            if n & 1:  # Odd length
                prev = node
            else:  # Even length
                curr, rev = prev.next, None
                for _ in range(n):  # Reverse the group
                    curr.next, rev, curr = rev, curr, curr.next
                prev.next.next, prev.next, prev = curr, rev, prev.next  # Connect the reversed group to other groups
            group_size += 1
        return head
