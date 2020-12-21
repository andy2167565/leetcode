# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # <Recursive Solution>
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2
        
        # <Iterative Solution>
        # Ref: https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode
        result = ListNode(0)
        result_tail = result
        
        while l1 and l2:
            if l1.val < l2.val:
                result_tail.next = l1
                l1 = l1.next
            else:
                result_tail.next = l2
                l2 = l2.next
            result_tail = result_tail.next
        
        if l1:
            result_tail.next = l1
        elif l2:
            result_tail.next = l2
        
        return result.next
