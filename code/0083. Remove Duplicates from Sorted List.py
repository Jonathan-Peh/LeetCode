# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return
        cache_val = head.val
        cache_add = head
        node = head
        while node:
            val = node.val
            if val == cache_val:
                cache_add.next = node.next
            else:
                cache_val = node.val
                cache_add = node
            node = node.next

        return head
