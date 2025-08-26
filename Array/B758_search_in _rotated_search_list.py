class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo=0
        hi=len(nums)-1
        mid=int((hi+lo+1)/2)
        
      
        
        while(lo<=hi):
             if target==nums[lo]:return lo
             if target==nums[hi]:return hi
             if target==nums[mid]:return mid
             if nums[lo]<=nums[mid]:
                
                  if target==nums[lo]:
                    return lo
                  elif target<nums[lo] or target>nums[mid]:  
                     lo=mid+1
                     mid=int((hi+lo+1)/2)
                  else:
                      hi=mid-1
                      mid=int((hi+lo+1)/2)   
  
             else   :
                 if target==nums[mid]:
                    return mid
                 elif target<nums[hi] and target>nums[mid]: 
                     lo=mid+1
                     mid=int((hi+lo+1)/2)
                 else:    
                     hi=mid-1
                     mid=int((hi+lo+1)/2)      
        return -1
