'''
Given a list of integers with no duplicates, find the max and set it as the root of a tree
The left subtree is then a tree built from the left partition of the list (list[0:max])
The right subtree is a tree build from the right partition of the remaining list (list[max+1:])
Return the root node
'''


class TreeNode():
	def __init__(self, num):
		self.val = num
		self.left = None
		self.right = None

class Solution:
    def constructMaxRoot(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def maxInd(arr):

        	currMax = arr[0]
        	maxInd = 0
        	leftArr = None
        	rightArr = None
        	for ind, val in enumerate(arr):
        		if val > currMax:
        			currMax = val
        			maxInd = ind
        	
        	if maxInd != 0:
        		leftArr = arr[0:maxInd]
        	if maxInd != len(arr) - 1:
        		rightArr = arr[maxInd + 1:]
        	return (currMax, leftArr, rightArr)

        def buildTree(node, val):
        	if val < node.val:
        		if node.left:
        			return buildTree(node.left, val)
        		else:
        			node.left = TreeNode(val)
        			return
        	else:
        		if node.right:
        			return buildTree(node.right, val)
        		else:
        			node.right = TreeNode(val)
        			return

        maxRoot, leftList, rightList = maxInd(nums)
        self.root = TreeNode(maxRoot)
        if leftList:
        	leftList.sort()
        	self.root.left = TreeNode(leftList.pop(len(leftList) - 1))
        if rightList:
        	rightList.sort()
        	self.root.right = TreeNode(rightList.pop(len(rightList) - 1))

        while leftList:
        	newVal = leftList.pop(len(leftList) - 1)
        	buildTree(self.root.left, newVal)

        while rightList:
        	newVal = rightList.pop(len(rightList) - 1)
        	buildTree(self.root.right, newVal)

        return self.root

newS = Solution()
print(newS.constructMaxRoot([3,2,1,6,0,5]).left.left.val)