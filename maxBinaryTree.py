'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree

Example:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
'''


class TreeNode():
	def __init__(self, num):
		self.val = num
		self.left = None
		self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.root = None
        def maxNode(node, dir, arr):
        	currMax = arr[0]
        	maxInd = 0
        	leftArr = None
        	rightArr = None
        	for ind, val in enumerate(arr):
        		if val > currMax:
        			currMax = val
        			maxInd = ind
        	newTree = TreeNode(currMax)
        	setattr(node, dir, newTree)
        	if maxInd != 0:
        		leftArr = arr[0:maxInd]
        		maxNode(getattr(node, dir), "left", leftArr)
        	if maxInd != len(arr) - 1:
        		rightArr = arr[maxInd + 1:]
        		maxNode(getattr(node, dir), "right", rightArr)
        	return

        maxNode(self, "root", nums)
        return self.root

newS = Solution()
newS.constructMaximumBinaryTree([3,2,1,6,0,5])
print(newS.root.right.left.val)