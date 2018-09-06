class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def recurCheck(node):
        	if node.left and node.right:
	        	if (node.left.left or node.left.right) and (node.right.left or node.right.right):
	        		node.left = recurCheck(node.left)
	        		node.right = recurCheck(node.right)
	        	elif node.left.left or node.left.right:
	        		node.left = recurCheck(node.left)
	        	elif node.right.left or node.right.left:
	        		node.right = recurCheck(node.right)
	        	else:
	        		if node.left and node.left.val != 1:
	        			node.left = None
	        		if node.right and node.right.val != 1:
	        			node.right = None
	        		return node
	        elif node.left:	        	
	        	node.left = recurCheck(node.left)
	        	return node
	        elif node.right:
	        	node.right = recurCheck(node.right)
	        	return node
	        else:
	        	if node.val != 1:
	        		return None
	        	else:
	        		return node
        recurCheck(root)
        return root

newTree = TreeNode(1)
newTree.left = TreeNode(0)
newTree.right = TreeNode(1)
newTree.left.left = TreeNode(0)
newTree.left.right = TreeNode(0)
newTree.right.left = TreeNode(0)
newTree.right.right = TreeNode(1)

newSol = Solution()
newSol.pruneTree(newTree)
print(newTree.left.val)