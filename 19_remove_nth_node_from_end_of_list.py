# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length = 0
        ptr = head
        while ptr is not None:
            length += 1
            ptr = ptr.next

        if n == length:
            return head.next

        ptr = head
        count = 0
        while ptr is not None:
            count += 1
            if count == (length - n):
                break
            ptr = ptr.next

        ptr.next = ptr.next.next

        return head


# ========================================================
solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
print solution.removeNthFromEnd(head, 3)
