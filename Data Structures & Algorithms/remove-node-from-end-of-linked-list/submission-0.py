# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1

        require = count - n 

        if require == 0 : # head case:
            head = head.next 
            return head

        index = 0
        temp1 = head
        while temp1:
            if index == require - 1:
                temp1.next = temp1.next.next
            temp1 = temp1.next
            index += 1
        return head

    