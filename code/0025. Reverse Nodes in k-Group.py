# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(next=head)
        last_terminal = dummy
        node = dummy

        while True:
            collected = []
            for i in range(k):
                node = node.next
                if not node:
                    return dummy.next
                collected.append(node)

            next_initial = collected[-1].next
            last_terminal.next = collected[-1]
            collected[0].next = next_initial
            last_terminal = collected[0]
            node = last_terminal

            for i in range(len(collected)-1,0,-1):
                collected[i].next = collected[i-1]
