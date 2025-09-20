# #User function Template for python3
# class Solution:
# 	def minDifference(self, arr):
# 		# code here
# 		total=sum(arr)
# 		N=len(arr)
# 		dp={}
		
# 		def solve(n,p1,total):
# 		    p2=total-p1
# 		    if n==0:
# 		        return abs(p1-p2)
# 		    elif (n,p1) in dp:
# 		        return dp[(n,p1)]
# 		    else:
# 		        item=arr[n-1]
# 		        if p1-item>=p2+item:
# 		            c1=solve(n-1,p1-item,total)
# 		            c2=solve(n-1,p1,total)
# 	                c= min(c1,c2)
# 		        else:
# 		            c=solve(n-1,p1,total)
# 		        return c
# 		return solve(N,total,total)    
		    
class Solution:
    def minDifference(self, arr):
        total = sum(arr)
        N = len(arr)

        # dp[j] = True if sum j is achievable
        dp = [False] * (total + 1)
        dp[0] = True

        for num in arr:
            # traverse backwards to avoid reuse of the same element
            for j in range(total, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True

        # check closest sum to total//2
        for j in range(total // 2, -1, -1):
            if dp[j]:
                return total - 2 * j
