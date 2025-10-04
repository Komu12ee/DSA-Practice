class Solution:
    def climbStairs(self, n: int) -> int:
        dp={}
        def solve(n):
            if n==0:
                return 1
            elif n<0:
                return 0   
            elif n in dp:
                return dp[n]     
            else:
                c1=solve(n-1)
                c2=solve(n-2)
                c=c1+c2    
                dp[n]=c
            return c    
