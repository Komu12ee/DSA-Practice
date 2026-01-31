# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         return self.binary(0, len(nums)-1, nums, target)

#     def binary(self, start, end, nums, target):

#         if start > end:
#             return -1

#         mid = (start + end) // 2

#         if nums[mid] == target:
#             return mid

#         elif nums[mid] < target:
#             return self.binary(mid+1, end, nums, target)

#         else:
#             return self.binary(start, mid-1, nums, target)


# OPTIMIZE 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(0, len(nums)-1, nums, target)

    def binary(self, start, end, nums, target):

        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            return self.binary(mid+1, end, nums, target)

        else:
            return self.binary(start, mid-1, nums, target)
