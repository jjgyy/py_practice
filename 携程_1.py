class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import sys
line = sys.stdin.readline().strip()
nodes = line.split(',')
head = ListNode('')
ptr = head
dict = {}

for node in nodes:
    if node in dict:
        ptr.next = dict[node]
    else:
        ptr.next = ListNode(node)
        dict[node] = ptr.next
    ptr = ptr.next

head = head.next
hasCircle = False
slow = head
fast = head

while (fast.next is not None) and (fast.next.next is not None):
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        hasCircle = True
        break

if hasCircle:
    print 'true'
else:
    print 'false'


    # class Solution(object):
    #     def getIntersectionNode(self, headA, headB):
    #         """
    #         :type head1, head1: ListNode
    #         :rtype: ListNode
    #         """
    #         if (headA is None) or (headB is None):
    #             return None
    #
    #         last = headA
    #         while last.next is not None:
    #             last = last.next
    #         last.next = headB
    #
    #         slow = headA
    #         fast = headA
    #
    #         hasCircle = False
    #         circleLength = 0
    #
    #         while (fast.next is not None) and (fast.next.next is not None):
    #             slow = slow.next
    #             fast = fast.next.next
    #             if slow == fast:
    #                 hasCircle = True
    #                 temp = slow
    #                 slow = slow.next
    #                 circleLength = 1
    #                 while slow != temp:
    #                     circleLength += 1
    #                     slow = slow.next
    #                 break
    #
    #         if not hasCircle:
    #             last.next = None
    #             return None