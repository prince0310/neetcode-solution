# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
     
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Handdle edge cases 
        if not root:
            return []

        # create queue 
        dq = deque([root])

        # An empty list in which we append the levels list 
        result = []

        # Iterating untill we have entry in deque
        while dq:

            # initialize a list to stroe the value of a level
            level = []

            # iterate through the entry of dq
            for i in range(len(dq)):
                # Fetch the node as per the order in queue
                node = dq.popleft()
                # append the value 
                level.append(node.val)

                # if the node has left child
                if node.left:
                    # append the left child into the queue
                    dq.append(node.left)
                
                # if node has right child 
                if node.right:
                    # append the left child into the queue
                    dq.append(node.right)

            # append the level into the result
            result.append(level)
        
        return result

             
 

        