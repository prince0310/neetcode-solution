# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        counter = 0
        has_map = {}
        temp1 = head
        while temp1:
            has_map[counter] = temp1
            temp1 = temp1.next
            counter += 1
        l = 1
        r = counter - 1 
        temp = head
        index = 1
        while l <= r:
            if index % 2 != 0:
                has_map[r].next = None
                temp.next = has_map[r] 
                temp = temp.next
                r -= 1
                index += 1
            else:
                has_map[l].next = None
                temp.next = has_map[l] 
                temp = temp.next
                l += 1
                index += 1
        temp.next = None
        
        

