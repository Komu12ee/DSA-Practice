class Solution:
    def findMin(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        mini=10000
        print("ok")
        while(left<=right):
            mid=(left+right)//2
            print(mid)
            if nums[left]<=nums[mid]:
                mini=min(mini,nums[left])
                left=mid+1
            elif nums[right]>nums[mid]:
                mini=min(mini,nums[mid])
                right=mid-1
        return mini            
        
