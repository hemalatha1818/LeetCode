# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue=[root]
        ans=[]
        if root==None:
            return []
        while queue:
            l=len(queue)
            f=0
            while l:
                root=queue.pop(0)
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)
                if f==0:
                    ans.append(root.val)
                    f=1    
                l-=1
        return ans