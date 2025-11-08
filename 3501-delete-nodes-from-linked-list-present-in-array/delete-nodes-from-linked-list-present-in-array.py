# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nums_sets= set(nums)
        while (head.val in nums_sets):
            head = head.next
        cur = head
        while(cur.next):
            if cur.next.val in nums_sets:
                cur.next = cur.next.next
            else :
                cur = cur.next
        return head
        