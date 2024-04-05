# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, s, e):
      if s > e:
        return [None]
      tree = []
      for i in range(s, e+1):
        lA = self.solve(s, i - 1)
        rA = self.solve(i + 1, e)

        for l in lA:
          for r in rA:
            root = TreeNode(i)
            root.left = l
            root.right = r
            tree.append(root)
      return tree

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
          return []
        return self.solve(1, n)