# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if (head is None) or (head.next is None):
            return head

        ptr1 = head
        ptr2 = head.next

        ptr1.next = self.swapPairs(ptr2.next)
        ptr2.next = ptr1

        return ptr2



# ========================================================
solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
ptr = solution.swapPairs(head)
while ptr is not None:
    print(ptr.val)
    ptr = ptr.next
