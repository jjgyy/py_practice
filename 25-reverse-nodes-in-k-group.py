# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        result = head
        if self.hasK(head, k):
            for _ in range(k - 1):
                result = result.next
        ptr = head
        while self.hasK(ptr, k):
            self.reverseList(ptr, k)
            tmp = ptr.next
            if self.hasK(ptr.next, k):
                for _ in range(k - 1):
                    ptr.next = ptr.next.next
            ptr = tmp

        return result

    def reverseList(self, head, k):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        ptr = head
        ptr2 = head.next
        for _ in range(k - 1):
            head.next = head.next.next
        # for _ in range(k - 1):
        #     head.next = head.next.next
        for _ in range(k - 1):
            tmp = ptr
            ptr = ptr2
            ptr2 = ptr.next
            ptr.next = tmp

        return ptr

    def hasK(self, head, k):
        ptr = head
        if head is None:
            return False
        for _ in range(k - 1):
            ptr = ptr.next
            if ptr is None:
                return False
        return True


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# ========================================================
solution = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node = solution.reverseKGroup(node1, 2)
while node is not None:
    print node.val,
    node = node.next
