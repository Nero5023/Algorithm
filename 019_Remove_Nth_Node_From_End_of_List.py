# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head
        for _ in range(0, n-1):
            fast = fast.next
        if fast.next is None:
            slow = slow.next
            return slow
        while fast.next.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
