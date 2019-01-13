# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        result = lists[0]
        for index in range(1, len(lists)):
            result = self.mergeTwoLists(result, lists[index])

        return result



    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        result = l1
        if l1.val <= l2.val:
            result = l1
            l1 = l1.next
        else:
            result = l2
            l2 = l2.next
        ptr = result

        while True:
            if (l1 is not None) and (l2 is not None):
                if l1.val <= l2.val:
                    ptr.next = l1
                    l1 = l1.next
                else:
                    ptr.next = l2
                    l2 = l2.next
                ptr = ptr.next
            else:
                if l1 is None:
                    ptr.next = l2
                else:
                    ptr.next = l1
                break

        return result



# ========================================================
solution = Solution()
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)

head2 = ListNode(2)
head2.next = ListNode(3)
head2.next.next = ListNode(5)

head3 = ListNode(2)
head3.next = ListNode(3)
head3.next.next = ListNode(5)

lists = [head1, head2, head3]

ptr = solution.mergeKLists(lists)
while ptr is not None:
    print(ptr.val)
    ptr = ptr.next


