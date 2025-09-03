class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # FIRST ATTEMPT FAILED
        # hsmap={}
        # l,r=1,1
        # maxi=0
        # prev=-1
        # while r<=len(s):
            
        #         if s[r-1] in hsmap:
        #          if prev!=r :
        #           hsmap[s[r-1]]+=1
        #         #   print(hsmap)   
        #           prev=r
        #          else:
        #             r+=1 
        #         else:
        #             hsmap[s[r-1]]=1 

        #         count=(r-l)+1
        #         print("diff",count-max(hsmap.values()))
        #         print(hsmap)
        #         if (count-max(hsmap.values()))<=k:
        #             maxi=max(count,maxi)
        #             r+=1
        #         else:
        #             hsmap[s[l-1]]-=1
        #             l+=1

        # # print(hsmap)
        # return maxi            

        #SECOND ATTEMPT
        count={}
        res=0
        l=0
        for r in range(len(s)):
         count[s[r]]=1+count.get(s[r],0)
         while(r-l+1)-max(count.values())>k:
            count[s[l]]-=1
            l+=1
         res=max(res,r-l+1)
        return res        