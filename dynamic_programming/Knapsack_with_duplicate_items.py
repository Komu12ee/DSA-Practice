#User function Template for python3

class Solution:
    def knapSack(self, val, wt,capacity):
        # code here
        N=len(val)
        W=capacity
        dp=[[0]*(W+1) for _ in range(N)]
        for i in range(N):
            for j in range(W+1):
                cap=j
                cv=val[i]
                cw=wt[i]
                if i==0:
                    dp[i][j]=(cap//cw)*cv
                else:
                    if cw<=cap:
                        dp[i][j]=max(cv+dp[i][cap-cw],dp[i-1][cap])
                    else:
                        dp[i][j]=dp[i-1][cap]
        return dp[N-1][W]            