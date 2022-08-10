# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#======== <Recursive Solution> ========#
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1)
            return list2
        
#======== <Iterative Solution> ========#
        # Ref: https://stackoverflow.com/questions/56515975/python-logic-of-listnode-in-leetcode
        result = ListNode(0)
        result_tail = result
        
        while list1 and list2:
            if list1.val < list2.val:
                result_tail.next = list1
                list1 = list1.next
            else:
                result_tail.next = list2
                list2 = list2.next
            result_tail = result_tail.next
        
        if list1:
            result_tail.next = list1
        elif list2:
            result_tail.next = list2
        
        return result.next
