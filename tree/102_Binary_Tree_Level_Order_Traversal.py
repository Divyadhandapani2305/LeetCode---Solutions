# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        queue = deque()
        queue.append(root)
        while queue:
            l =[]
            size = len(queue)
            for _ in range(size):
                a = queue.popleft()
                l.append(a.val)
                if (a.left):
                    queue.append(a.left)
                if (a.right):
                    queue.append(a.right)
            result.append(l)
        return result
        
