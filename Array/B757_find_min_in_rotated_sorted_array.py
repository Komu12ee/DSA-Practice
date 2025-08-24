class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        mid= int((start+end)/2)
        mnm=min(nums[start],nums[end])
        while(start<=end):
         
         if nums[mid]>=nums[start] :  
            mnm=min(nums[start],mnm)  
            start=mid+1
            mid=int((start+end)/2 )
           
         else:
            mnm=min(nums[mid],mnm)
            end=mid-1
            mid=int((start+end)/2 )
            mnm=min(nums[end],mnm)
           
        return mnm