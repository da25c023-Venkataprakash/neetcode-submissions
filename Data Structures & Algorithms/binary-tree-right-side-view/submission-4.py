# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def bfs(node):
            if node is None:
                return []
            q = deque([node])
            res=[]

            while q:
                level_length = len(q)
                for i in range(level_length):
                    ele = q.popleft()
                    if i == (level_length - 1):
                        res.append(ele.val)
                    if ele.left: 
                        q.append(ele.left)
                    if ele.right:
                        q.append(ele.right)
            return res
        return bfs(root)
                    

        
