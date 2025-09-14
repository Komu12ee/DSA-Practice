# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         l=0
#         r=len(nums)-1
#         while l<=r:
#             mid=(l+r)//2
#             if target==nums[mid]:
#                 return True
#             elif target<nums[mid] and nums[mid]>nums[l] :
#                 if  target<nums[l]:
#                     l=mid+1    
#                 else:
#                     r=mid-1
#             elif  target<nums[mid] and nums[mid]<nums[l]  :
#                  r=mid-1      
#             elif target>nums[mid] and nums[mid]>nums[l] :
#                     l=mid+1    
              
#             elif  target>nums[mid] and nums[mid]<nums[l]  :
#                 if target<nums[r]:
              
#                  l=mid+1   
#                 else :
#                   r=mid-1
#         return False          

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return True
            
            # Handle duplicates
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[mid]:  # Left half sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # Right half sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return False
