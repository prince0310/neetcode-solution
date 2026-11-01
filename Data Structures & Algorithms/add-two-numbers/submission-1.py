# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # option 1 - find number and make a linked list out of it
        # unit1 = 1
        # num1 = 0
        # while l1:
        #     num1 += unit1 * l1.val
        #     l1 = l1.next
        #     unit1 *= 10

        # unit2 = 1
        # num2 = 0
        # while l2:
        #     num2 += unit2 * l2.val
        #     l2 = l2.next
        #     unit2 *= 10

        # final = str(num1 + num2)[: :-1]
        # n = len(final) - 1
        # head = ListNode(int(final[0]))
        # temp = head
        # x = 0
        # while x < n:
        #     x += 1
        #     temp.next = ListNode(int(final[x]))
        #     temp = temp.next

        # return head

        # Option 2 in place
        temp1 = l1
        temp2 = l2

        count1 = 0
        while temp1:
            count1 += 1
            temp1 = temp1.next

        count2 = 0
        while temp2:
            count2 += 1
            temp2 = temp2.next
        
        if count2 > count1:
            l1 , l2 = l2, l1

        head = l1

        carry = 0
        prev = None
        while l1 or l2 :
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sumation = v1 + v2 + carry
            value  = sumation % 10
            
            carry  = sumation // 10
            if l1:
                l1.val = value
                prev  = l1
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry :
            prev.next = ListNode(carry)
        return head
            

 

        

            
               



        
        