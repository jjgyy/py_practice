# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        if head is None:
            return None
        """
        :type head: ListNode
        :rtype: ListNode
        """
        array = []
        ptr = head
        while ptr is not None:
            array.append(ptr.val)
            ptr = ptr.next

        array.sort()
        head.val = array[0]
        ptr = head
        for index in range(1, len(array)):
            ptr.next.val = array[index]
            ptr = ptr.next

        return head

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# ========================================================
solution = Solution()
head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(1)
node = solution.sortList(head)
while node is not None:
    print node.val,
    node = node.next
