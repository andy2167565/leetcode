# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
#======== <Solution 1> ========#
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/palindrome-linked-list/discuss/1137027/JS-Python-Java-C%2B%2B-or-Easy-Floyd's-%2B-Reversal-Solution-w-Explanation
        reverse_last = None
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        # Reverse the last half of the linked list and pointed by reverse_last
        while slow:
            reverse_last, reverse_last.next, slow = slow, reverse_last, slow.next
        while reverse_last and head.val == reverse_last.val:
            head, reverse_last = head.next, reverse_last.next
        return not reverse_last

# Reference: https://leetcode.com/problems/palindrome-linked-list/discuss/64500/11-lines-12-with-restore-O(n)-time-O(1)-space
#======== <Solution 3> ========#
        reverse_first = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            # Reverse the first half of the linked list and pointed by reverse_first. Same as follows:
            # tmp = reverse_first
            # reverse_first = slow
            # slow = slow.next
            # reverse_first.next = tmp
            reverse_first, reverse_first.next, slow = slow, reverse_first, slow.next
        # fast is not None: Linked list with odd number of nodes. Move slow from the middle node to the next node
        # fast is None: Linked list with even number of nodes. slow will be at right of the middle two nodes
        if fast:
            slow = slow.next
        # Compare the reversed first half with the second half
        while reverse_first and reverse_first.val == slow.val:
            slow, reverse_first = slow.next, reverse_first.next
        return not reverse_first

#======== <Solution 4> ========#
        rev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, head = head, rev, head.next
        tail = head.next if fast else head
        isPali = True
        # Restore the list to its original state by reversing the first half back while comparing the two halves
        while rev:
            isPali = isPali and rev.val == tail.val
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return isPali
