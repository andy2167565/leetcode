# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Reference: https://leetcode.com/problems/reverse-linked-list/discuss/246827/Python-Iterative-and-Recursive
#======== <Solution 1> ========#
        # Reference (Explanation): https://leetcode.com/problems/reverse-linked-list/discuss/803955/C%2B%2B-Iterative-vs.-Recursive-Solutions-Compared-and-Explained-~99-Time-~85-Space
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

#======== <Solution 2> ========#
        if not head or not head.next:
            return head
        reverse = self.reverseList(head.next)  # reverse points at the last node of the linked list
        head.next.next = head  # Link head.next to head [1]
        head.next = None  # Break the link between head and head.next to eliminate the cycle [2]
        return reverse
        # e.g.
        # 1st Round:                        [1]                      ↓￣￣|      [2]                      ↓￣￣￣￣￣￣|
        # 1 -> 2 -> 3 -> 4 -> 5 -> None     ===>      1 -> 2 -> 3 -> 4 -> 5      ===>      1 -> 2 -> 3 -> 4 -> None   5
        #                ↑    ↑                                      ↑    ↑                               ↑           ↑
        #                head reverse                                head reverse                         head        reverse
        #
        # 2nd Round:
        #                ↓￣￣￣￣￣￣|      [1]                 ↓￣￣|           [2]                 ↓￣￣￣￣￣￣|
        # 1 -> 2 -> 3 -> 4 -> None   5      ===>      1 -> 2 -> 3 -> 4 <- 5      ===>      1 -> 2 -> 3 -> None   4 <- 5
        #           ↑                ↑                          ↑         ↑                          ↑                ↑
        #           head             reverse                    head      reverse                    head             reverse
