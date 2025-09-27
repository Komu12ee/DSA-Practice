
class Solution:
    def count(self, coins, sum):
        # code here 
        N=len(coins)
        dp={}
        def solve(n,cap):
            if cap==0:
                return 1
            elif n==0:
                return 0
            elif (n,cap) in dp:
                return dp[(n,cap)]
            else:
                val=coins[n-1]
                if val<=cap:
                    c1=solve(n,cap-val)
                    c2=solve(n-1,cap)
                    c=c1+c2
                else:
                    c=solve(n-1,cap)
                dp[(n,cap)]=c
                return c    
        return solve(N,sum)
