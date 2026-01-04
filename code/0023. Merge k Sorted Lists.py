# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# could have used a min-heap
class Solution(object):
    def mergeKLists(self, lists):
        head = ListNode()
        node = head

        while True:
            min_val = (None,None) # value, list index
            ends = 0
            for lis in range(len(lists)):
                if not lists[lis]:
                    ends += 1
                    continue
                val = lists[lis].val
                if min_val[0] is None or val < min_val[0]:
                    min_val = (val,lis)
            if ends == len(lists):
                return head.next

            node.next = lists[min_val[1]]
            node = node.next
            lists[min_val[1]] = lists[min_val[1]].next
