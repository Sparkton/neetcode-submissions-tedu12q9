# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxHeight = 0
        def dfsHeight(node: TreeNode) -> int:
            if not node:
                return -1
            dfs_left = dfsHeight(node.left)
            dfs_right = dfsHeight(node.right)
            max_height = 2 + dfs_left + dfs_right
            self.maxHeight = max(self.maxHeight, max_height)
            return 1 + max(dfs_left, dfs_right)

        dfsHeight(root)
        return self.maxHeight