# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Reference: https://leetcode.com/problems/merge-k-sorted-lists/solutions/1032723/python-heap-solution-explained/
        import heapq
        dummy = curr = ListNode(0)
        heap = []
        for i, ls in enumerate(lists):  # Put all starts of k linked lists to heap
            if ls:
                heapq.heappush(heap, (ls.val, i))
        while heap:
            num, idx = heapq.heappop(heap)  # Get current minimum element from heap
            curr.next = ListNode(num)
            curr = curr.next
            if lists[idx].next:  # Put the next value of lists[idx] into heap
                lists[idx] = lists[idx].next
                heapq.heappush(heap, (lists[idx].val, idx))
        return dummy.next
