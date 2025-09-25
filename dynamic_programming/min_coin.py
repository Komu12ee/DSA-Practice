# #User function Template for python3

# class Solution:
# 	def MinCoin(self, nums, amount):
# 		# Code here
# 	 nums.sort(reverse=True)	
# 	 N=len(nums)
# 	 dp={}
# 	 def solve(n,amt):	
# 		if amt==0:
# 		    return 0
# 		elif n==0:
# 		    return float('INF')
# 		elif (n,amt) in dp:
# 		    return dp[(n,amt)]
# 		else:
# 		    val=nums[n-1]
# 		    if val<=amt:
# 		        c1=1+solve(n,amt-val)
# 		        c2=solve(n-1,amt)
# 		        c=min(c1,c2)
# 		    else:
# 		        c=solve(n-1,amt)
# 		    dp[(n,amt)]=c
# 		    return c
		    
# 	 val = solve(N,amount)
# 	 if val>=10**9+7:
# 	     return -1
# 	 else:
# 	     return val

class Solution:
    def MinCoin(self, nums, amount):
        # Initialize DP array with INF
        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0   # 0 coins to make 0

        # Process each coin
        for coin in nums:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], 1 + dp[x - coin])

        return -1 if dp[amount] == INF else dp[amount]
