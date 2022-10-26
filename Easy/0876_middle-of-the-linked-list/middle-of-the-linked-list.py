# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#======== <Solution 1> ========#
        node_list = []
        while head:
            node_list.append(head)
            head = head.next
        return node_list[len(node_list) // 2]

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/middle-of-the-linked-list/discuss/1651785/C%2B%2BPython-Simple-Solution-w-Explanation-or-Brute-Force-%2B-Single-Pass-using-Slow-and-Fast-Pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
