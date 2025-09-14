# class Solution:
#     def knapsack(self, W, val, wt):
#         # code here
#         dp={}
#         n=len(val)
#         def solve(n,cap):
#             if n==0 or cap==0:
#                 return 0
#             elif (n,cap) in dp:
#                 return dp[(n,cap)]
#             else:
#                 cwt=wt[n-1]
#                 cv=val[n-1]
#                 if cwt<=cap:
#                     c1=cv+solve(n-1,cap-cwt)
#                     c2=solve(n-1,cap)
#                     c= max(c1,c2)
#                 else:
#                     c= solve(n-1,cap)
#                 dp[(n,cap)]=c
#                 return c
#         return solve(n,W)            
                
#   ..............ABOVE CODE IS WORK FINE BUT AFTER 1111 CASE IT EXCEED MEMORY LIMIT.............
class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)

        # Create memo table initialized with -1
        dp = [[-1] * (W + 1) for _ in range(n + 1)]

        def solve(i, cap):
            # Base case
            if i == 0 or cap == 0:
                return 0

            # If already solved → return stored value
            if dp[i][cap] != -1:
                return dp[i][cap]

            # Current item details
            cwt = wt[i - 1]
            cv = val[i - 1]

            if cwt <= cap:
                # Option 1: take the item
                take_it = cv + solve(i - 1, cap - cwt)
                # Option 2: leave the item
                leave_it = solve(i - 1, cap)
                dp[i][cap] = max(take_it, leave_it)
            else:
                # Item too heavy → skip
                dp[i][cap] = solve(i - 1, cap)

            return dp[i][cap]

        return solve(n, W)
