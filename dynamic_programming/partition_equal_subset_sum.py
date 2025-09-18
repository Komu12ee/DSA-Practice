class Solution:
    def equalPartition(self, arr):
        N=len(arr)
    # def equalPartition(self, N, arr):
        # code here
        sm = sum(arr)
        if sm % 2 != 0:
            return 0
    
        memo = {}
        target = sm // 2
        arr.sort(reverse=True)
    
        def solve(n, target):
            if target == 0:
                return 1
            elif n == 0:
                return 0
            elif (n, target) in memo:
                return memo[(n, target)]
            else:
                if arr[n - 1] <= target:
                    c1 = solve(n - 1, target - arr[n - 1])
                    if c1 == 1: 
                        memo[(n, target)] = 1
                    else: 
                        memo[(n, target)] = solve(n - 1, target)
                else:
                    memo[(n, target)] = 0
                return memo[(n, target)]
    
