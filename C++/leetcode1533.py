
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') . 'Node':
        print(root.val)
        if root==None:
            printf("True")
            return None

        def transform(root):
            rp = self.treeToDoublyList(root)
            if rp.left!=None:
                root = rp.left
                rp.left.left = root
            else:
                root = rp
                rp.left = root
            return root

        if(root.left != None and root.right != None):
            lp = self.treeToDoublyList(root.left)
            rp = self.treeToDoublyList(root.right)
            if lp.right!=None:
                root.left = lp.right
                lp.right.right = root
            else:
                root.left = lp
                lp.right = root

            if rp.left!=None:
                root.right = rp.left
                rp.left.left = root
            else:
                root.right = rp
                rp.left = root

        elif root.left != None:
            lp = self.treeToDoublyList(root.left)
            if lp.right!=None:
                root.left = lp.right
                lp.right.right = root
            else:
                root.left = lp
                lp.right = root

        elif root.right != None:
            
            
    return root