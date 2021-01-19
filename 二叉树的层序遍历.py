# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# BFS 广度优先搜索
class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        res=[]
        if (root):
            queue=[root]
        else:
            return []
        while(queue):
            length=len(queue)
            rowlist=[]
            for _ in range(length):
                elem=queue.pop(0)
                rowlist.append(elem.val)
                if(elem.left!=None):
                    queue.append(elem.left)
                if(elem.right!=None):
                    queue.append(elem.right)
            res.append(rowlist)
        return res

