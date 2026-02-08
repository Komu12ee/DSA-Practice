class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>nums[left] and nums[mid]>target and nums[left]<=target:
                right=mid-1
            elif nums[mid]<nums[right] and nums[mid]<target and nums[right]<target:
                right=mid-1  

            elif nums[mid]<nums[right] and nums[mid]>target and nums[right]>target:
                right=mid-1       
            else: 
                left=mid+1
        return -1    
