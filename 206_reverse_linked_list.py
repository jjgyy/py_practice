# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        ptr = head
        ptr2 = head.next
        head.next = None
        while ptr2 is not None:
            tmp = ptr
            ptr = ptr2
            ptr2 = ptr.next
            ptr.next = tmp

        return ptr



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# =============================================
solution = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node = solution.reverseList(node1)
while node is not None:
    print node.val,
    node = node.next
