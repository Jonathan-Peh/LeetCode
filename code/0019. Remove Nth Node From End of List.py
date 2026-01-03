# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        new_start_pos = length - n - 1
        new_end_pos = length - n + 1
        new_start = None
        new_end = None

        node = head
        pos = 0
        while node:
            if pos == new_start_pos:
                new_start = node
            if pos == new_end_pos:
                new_end = node
                break
            pos += 1
            node = node.next

        if new_start:
            if new_end:
                new_start.next = new_end
                return head
            else:
                new_start.next = None
                return head
        elif new_end:
            return new_end
