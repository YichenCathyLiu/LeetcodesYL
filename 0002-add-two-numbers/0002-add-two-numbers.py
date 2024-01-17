# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode() # 新建链表的固定操作
        current = head

        carry = 0
        while (l1!=None or l2!=None or carry!=0):# 还有的加，或者是有进位
            l1_value = l1.val if l1 else 0
            l2_value = l2.val if l2 else 0
            total = l1_value + l2_value +carry # 相加的操作，包括进位的部分
            current.next = ListNode(total%10) # create new listnode to hold the answer
            carry = total//10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
        return head.next
