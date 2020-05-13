matrix=[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

dp=[[0 for i in matrix[0]]for i in matrix]
for i in range(len(dp)):
    for j in range(len(dp[0])):
        if matrix[i][j]=="0":
            pass
        else:
            dp[i][j]=dp[i][j-1]+1
