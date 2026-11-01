# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # option 1 - find number and make a linked list out of it
        unit1 = 1
        num1 = 0
        while l1:
            num1 += unit1 * l1.val
            l1 = l1.next
            unit1 *= 10

        unit2 = 1
        num2 = 0
        while l2:
            num2 += unit2 * l2.val
            l2 = l2.next
            unit2 *= 10

        final = str(num1 + num2)[: :-1]
        n = len(final) - 1
        head = ListNode(int(final[0]))
        temp = head
        x = 0
        while x < n:
            x += 1
            temp.next = ListNode(int(final[x]))
            temp = temp.next

        return head
            



        
        