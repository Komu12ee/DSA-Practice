#User function Template for python3

class Solution:
    def findTargetSumWays(self, n, arr, target):
        # code here 
        SUM =sum(arr)
        x=SUM+target
        if x%2!=0:
            return 0
        else:
            x=x//2
        dp={}    
        arr.sort(reverse=True)    
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
                    c=c1+c2
                else:
                    if sm==0:
                        c=1
                    else:
                        c=0
                dp[(n,sm)]=c    
                return c
        return solve(n,x)        