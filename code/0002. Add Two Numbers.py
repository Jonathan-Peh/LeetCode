# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        value = l1.val + l2.val
        l1 = l1.next
        l2 = l2.next
        carryOver, value = value//10, value%10
        l3 = ListNode(value)
        before = l3
        while l1 or l2:
            value = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carryOver
            carryOver, value = value//10, value%10
            before.next = ListNode(value)
            before = before.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if carryOver:
            before.next = ListNode(carryOver)
        return l3
