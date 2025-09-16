class Solution:
    def knapSack(self, W, wt, val, N):
        dp = [[0]*(W+1) for _ in range(N)]

        for i in range(N):
            for j in range(W+1):
                cap = j
                cwt = wt[i]
                cv = val[i]
                if i == 0:
                    if cwt <= cap:
                        dp[i][j] = cv
                    else:
                        dp[i][j] = 0
                else:
                    if cwt <= cap:
                        c1 = cv + dp[i-1][cap-cwt]
                        c2 = 0 + dp[i-1][cap]
                        dp[i][j] = max(c1, c2)
                    else:
                        dp[i][j] = dp[i-1][cap]
        
        return dp[N-1][W]
