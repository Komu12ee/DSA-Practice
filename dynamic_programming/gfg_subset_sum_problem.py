class Solution:
    def isSubsetSum(self, arr, target):
        N = len(arr)
        dp = [[0] * (target + 1) for _ in range(N)]

        # base case
        for i in range(N):
            dp[i][0] = 1   # sum 0 is always possible
        
        if arr[0] <= target:
            dp[0][arr[0]] = 1

        # fill table
        for i in range(1, N):
            for sm in range(1, target + 1):
                not_take = dp[i-1][sm]
                take = 0
                if arr[i] <= sm:
                    take = dp[i-1][sm-arr[i]]
                dp[i][sm] = take or not_take

        return dp[N-1][target]

# class Solution:
#     def isSubsetSum(self, arr, sum):
#         N = len(arr)
#         dp = [(0) * [sum+1] for _ in range(N)]
#         for i in range(N):
#             for j in range(sum+1):
#                 item=arr[i]
#                 sm=j
#                 if i==0:
#                     if sm==0 or item==sm:
#                         dp[i][j]=1
#                     else:
#                         if item<=sm:
#                             dp[i][j]=dp[i-1][sm-item] or dp[i-1][sm]
#                         else:
#                             dp[i][j]=dp[i-1][sm]
#         return dp[N-1][sum]                    
                            
