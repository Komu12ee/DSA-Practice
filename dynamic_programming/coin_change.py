
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
# from typing import List

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         N = len(coins)
#         dp = {}

#         def solve(n, amt):
#             # Base cases
#             if amt == 0:
#                 return 0   # 0 coins needed
#             if n < 0:     # no coins left
#                 return float('inf')

#             if (n, amt) in dp:
#                 return dp[(n, amt)]

#             cval = coins[n]

#             if cval <= amt:
#                 # Option 1: take coin
#                 c1 = 1 + solve(n, amt - cval)
#                 # Option 2: skip coin
#                 c2 = solve(n - 1, amt)
#                 dp[(n, amt)] = min(c1, c2)
#             else:
#                 dp[(n, amt)] = solve(n - 1, amt)

#             return dp[(n, amt)]

#         ans = solve(N - 1, amount)
#         return ans if ans != float('inf') else -1


from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        
        # Step 1: Initialize DP table
        INF = float('inf')
        dp = [[INF] * (amount + 1) for _ in range(N + 1)]
        
        # Step 2: Base case: amount = 0 requires 0 coins
        for i in range(N + 1):
            dp[i][0] = 0

        # Step 3: Fill DP table
        for i in range(1, N + 1):
            for j in range(1, amount + 1):
                cval = coins[i-1]   # current coin value
                
                if cval <= j:
                    # Option 1: take the coin (stay at i, reduce amount)
                    # Option 2: skip the coin (move to i-1)
                    dp[i][j] = min(1 + dp[i][j - cval], dp[i-1][j])
                else:
                    # Can't take this coin, so skip it
                    dp[i][j] = dp[i-1][j]

        # Step 4: Answer is in dp[N][amount]
        return dp[N][amount] if dp[N][amount] != INF else -1
