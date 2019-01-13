# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA is None) or (headB is None):
            return None

        last = headA
        while last.next is not None:
            last = last.next
        last.next = headB

        slow = headA
        fast = headA

        hasCircle = False
        circleLength = 0

        while (fast.next is not None) and (fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCircle = True
                temp = slow
                slow = slow.next
                circleLength = 1
                while slow != temp:
                    circleLength += 1
                    slow = slow.next
                break

        if not hasCircle:
            last.next = None
            return None

        slow = headA
        fast = headA
        for _ in range(circleLength):
            fast = fast.next

        while True:
            if slow == fast:
                last.next = None
                return slow
            slow = slow.next
            fast = fast.next


# ========================================================
solution = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
headA = node1
headA.next = node2
headA.next.next = node3
headB = headA
print solution.getIntersectionNode(headA, headB).val
