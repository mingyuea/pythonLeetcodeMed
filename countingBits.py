from math import floor, log

class Solution:
    def countBits(self, num):
        """
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:
Input: 2     Output: [0,1,1]

Example 2:
Input: 5     Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
        """

        startArr = [0, 1, 1, 2]

        if num > 3:
        	for currNum in range(4, num+1):
        		currInd = currNum - 2**floor(log(currNum, 2))
        		bitCount = startArr[currInd] + 1
        		startArr.append(bitCount)
        	return startArr
        else:
        	return startArr[0:num+1]

newSol = Solution()
print(newSol.countBits(3))