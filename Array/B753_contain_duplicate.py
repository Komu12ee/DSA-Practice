class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset=set()
        for i,n in enumerate (nums):
            if( nums[i] in myset):
               
                return True
            else:
                myset.add(n)
       
        return False     