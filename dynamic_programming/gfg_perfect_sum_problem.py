#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
		# code hereN
		dp={}
		N=len(arr)
		def solve(n,sm):
		    if n==0:
		        if sm==0:
		            return 1
		        else:      
		          return 0
		    elif (n,sm) in dp:   
		        return dp[(n,sm)]
		    else: 
		        item=arr[n-1]
		        if item<=sm:
		            c1=solve(n-1,sm-item)
		            c2=solve(n-1,sm)
		            c= c1+c2
		        else:
		            c1=solve(n-1,sm)
		            c= c1
		        dp[(n,sm)]=c
		        return c        
		    
		
