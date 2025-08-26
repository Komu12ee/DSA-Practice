class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_list=[]
        n=len(nums)
        for i in range(n):
            if nums[i]>0:
                break
            elif i>0 and nums[i]==nums[i-1]:
                continue    
            j=i+1
            last_index=n-1
            while(j<last_index):

              low=nums[j]
              high=nums[last_index]
              if low+high+nums[i]==0  :
                lst=[nums[i],nums[j],nums[last_index]]
                # print(lst)
                final_list.append(lst)
                j=j+1
                print(j)
                last_index-=1
                while  j<last_index and nums[j]==nums[j-1]:
                    j+=1
                while j<last_index and nums[last_index]==nums[last_index+1]:
                    last_index-=1
              elif low+high+nums[i]>0 :
                last_index=last_index-1

              elif low+high+nums[i]<0:
                j=j+1  
              
        return final_list