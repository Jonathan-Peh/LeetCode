# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        left = head
        last_terminal = None
        
        while left and left.next:
            right = left.next
            if last_terminal:
                last_terminal.next = right
            else:
                head = right
            last_terminal = left
            next_initial = right.next
            right.next = left
            left.next = next_initial
            left = next_initial
            
        return head
            
