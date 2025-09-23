class Solution:
    def cutRod(self, price):
        N = len(price)
        dp = [0] * (N + 1)

        # dp[j] = max profit for rod length j
        for i in range(1, N + 1):       # each piece length
            for j in range(i, N + 1):   # rod length >= i
                dp[j] = max(dp[j], price[i-1] + dp[j-i])

        return dp[N]
