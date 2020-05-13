#https://leetcode.com/problems/maximal-rectangle/
matrix=[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
     
#DP O(N^2*M)       
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp=[[0 for i in matrix[0]]for i in matrix]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if matrix[i][j]=="0":
                    pass
                else:
                    dp[i][j]=dp[i][j-1]+1
        maxSpace=0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                curSpace=0
                curWidth=10e8
                for k in range(i,-1,-1):
                    curWidth=min(curWidth,dp[k][j])
                    curSpace=curWidth*(i-k+1)
                    maxSpace=max(curSpace,maxSpace)
        return maxSpace
    
#Reduce some time usage by merge the dp matrix construction and the maxSpace calculation       
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        dp=[[0 for i in matrix[0]]for i in matrix]
        maxSpace=0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if matrix[i][j]=="0":
                    pass
                else:
                    dp[i][j]=dp[i][j-1]+1
                    curSpace=0
                    curWidth=10e8
                    for k in range(i,-1,-1):
                        curWidth=min(curWidth,dp[k][j])
                        curSpace=curWidth*(i-k+1)
                        maxSpace=max(curWidth*(i-k+1),maxSpace)
        return maxSpace
