# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        node1 = list1
        node2 = list2
        head = ListNode()
        node3 = head
        while node1 and node2:
            if node1.val > node2.val:
                node3.next = node2
                node2 = node2.next
            else:
                node3.next = node1
                node1 = node1.next
            node3 = node3.next
        while node1 or node2:
            if node1:
                node3.next = node1
                node1 = node1.next
                node3 = node3.next
            elif node2:
                node3.next = node2
                node2 = node2.next
                node3 = node3.next
        return head.next
