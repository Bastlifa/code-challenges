# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        a = []
        starting = [root]
        # a.append(starting)
        
        def child_list(level):
            b = []
            for n in level:
                if n is not None:
                    if n.left is not None:
                        b.append(n.left)
                    if n.right is not None:
                        b.append(n.right)
            
            return b
        
        finished = False
        while not finished:
            c = []
            for n in starting:
                if n is not None:
                    c.append(n.val)
            if len(c) > 0:
                a.insert(0, c)
            starting = child_list(starting)
            if len(starting) == 0:
                finished = True
                
        # print(a)
        return a