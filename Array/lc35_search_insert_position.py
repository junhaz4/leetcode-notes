class Solution:
    def searchinsetposition(self, nums: list[int], target: int) -> list[int]:
        # [left,right]
        # stop criterion is left>right and nums[right=<target<nums[left], left is the position
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return -1