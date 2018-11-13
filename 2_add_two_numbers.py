# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l2 is None) & (l1 is None):
            return
        if (l2 is None) & (l1 is not None):
            while l1.val > 9:
                l1.val -= 10
                if l1.next is not None:
                    l1.next.val += 1
                    l1 = l1.next
                else:
                    l1.next = ListNode(1)
            return

        l1.val += l2.val
        if l1.val > 9:
            if l1.next is None:
                l1.next = ListNode(1)
            else:
                l1.next.val += 1

            l1.val -= 10

        # python pointer point at storage position, not variable position
        if (l1.next is None) & (l2.next is not None):
            l1.next = l2.next
            return l1

        self.addTwoNumbers(l1.next, l2.next)

        return l1


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


solution = Solution()
l1 = ListNode(9)
l2 = ListNode(9)
l3 = ListNode(9)
l1.next = l3
print solution.addTwoNumbers(l1, l2).next.val
