# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
# Reference: https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/solutions/366319/java-c-python-greedily-skip-with-hashmap/
#======== <Solution 1> ========#
        import collections
        curr = dummy = ListNode(0)
        dummy.next = head
        seen, prefix = collections.OrderedDict(), 0
        while curr:
            prefix += curr.val
            node = seen.get(prefix, curr)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = curr = curr.next
        return dummy.next

#======== <Solution 2> ========#
        seen, prefix = {}, 0
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next
        head, prefix = dummy, 0
        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        return dummy.next
