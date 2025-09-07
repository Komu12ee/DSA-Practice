B75
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         sum=0
#         j=1
#         while j<=len(s):
#             print(j)
#             l,r=0,0
#             while l<len(s):
#              r=l
#              for i in range(j):
#                 if i+1==j:
#                     sum+=1
#                 elif not(s[l]==s[r]):
#                     r+=i 
#                     break
#                 r+=i   
#              l+=1       

#             j+=1            
#         return sum
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        res = 0
        for i in range(len(s)):
            # Odd length palindrome
            res += expand(i, i)
            # Even length palindrome
            res += expand(i, i + 1)
        return res

