class Solution:
    def findDuplicates(self, nums):
        """
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
        """

        existDict = {}
        dupArr = []

        for num in nums:
        	if num in existDict:
        		dupArr.append(num)
        	else:
        		existDict[num] = 1
        return dupArr
newSol = Solution()
print(newSol.findDuplicates([4,3,2,7,8,2,3,1]))
