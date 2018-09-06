class Solution:
    def matrixScore(self, A):
        """
We have a two dimensional matrix A where each value is 0 or 1.
A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score.

Example 1:
Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]] which is 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
        """

        def firstCol(matrix):
        	for row in matrix:
        		if row[0] == 0:
        			for ind in range(len(row)):
        				row[ind] ^= 1
        	return

        def nextCol(matrix):
        	colNum = len(matrix[0])
        	for col in range(1, colNum):
        		colSum = 0
        		for row in matrix:
        			colSum += row[col]
        		if colSum < len(matrix)/2:
        			for row in matrix:
        				row[col] ^= 1
        	return

        def binSum(matrix):
        	totalSum = 0
        	for row in matrix:
        		binStr = ""
        		for elem in row:
        			binStr += str(elem)
        		totalSum += int(binStr, 2)
        	return totalSum


        firstCol(A)
        nextCol(A)
        return binSum(A)

S = Solution()
newM = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(S.matrixScore(newM))
