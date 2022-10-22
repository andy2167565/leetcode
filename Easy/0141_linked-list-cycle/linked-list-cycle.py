# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#======== <Solution 1> ========#
        nodeSet = set()
        while head:
            if head in nodeSet:
                return True
            nodeSet.add(head)
            head = head.next
        return False

#======== <Solution 2> ========#
        while head:
            if head.val == 'busted':
                return True
            head.val = 'busted'
            head = head.next
        return False

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/linked-list-cycle/discuss/1047852/Python-two-pointers-O(1)-memory-explained
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                return True
        return False
