# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         count=0
#         exp=0
#         for i in range(len(wordDict)):
#             if wordDict[i] in s:
#                 s=s.replace(wordDict[i],"")
#                 count+=1 
#             else:
#                 exp+=1
#         if s=="" or count==len(wordDict) or count>0:
#          print(count,s)       
#          return True
#         else :
#             return False  



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # empty string can be segmented

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
