# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         maxi=max(nums)
#         prev=nums[0]
#         mul=1
#         lst=[]
#         for i in range(len(nums)):
#             mul=mul*nums[i]
#             if mul <= prev:
#                 # lst.append(maxi)
#                 prev=nums[i+1]
#                 mul=nums[i+1]
#             else:
#                 if mul>maxi:
#                     prev=maxi
#                     maxi=mul

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curmin,curmax=1,1
        for n in nums:
            if n==0:
                curmin,curmax=1,1
                continue
            tmp=curmax*n
            curmax=max(n*curmax,n*curmin,n)
            curmin=min(tmp,n*curmin,n)
            res=max(res,curmax)
        return res

        
            
