class Solution:
    def searchRange(self, nums: list[int], target: int):
        '''
        # case 1: target in the left or right of the interval, return [-1,-1]
        # case 2: target inside the interval, but not in nums, return[-1,-1]
        # case 3: target inside the interval and in nums
        '''
        # Method 1
        def getLeft(nums,target):
            left = 0
            right = len(nums)-1
            leftBoarder = None
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] >= target:
                    right = mid-1
                    leftBoarder = right
                else:
                    left = mid+1
            return leftBoarder

        def getRight(nums,target):
            left = 0
            right = len(nums)-1
            rightBoarder = None
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
                    rightBoarder = left
            return rightBoarder

        left = getLeft(nums,target)
        right = getRight(nums,target)

        if left==None or right==None:
            return [-1.-1]
        if right-left>1:
            return [left+1,right-1]
        else:
            return[-1,-1]

        # Method 2
        def binary_search(nums,target,lower):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    index = mid
                    if lower:
                        right = mid
                    else:
                        left = mid+1
            return index
        left = binary_search(nums,target,True)
        right = binary_search(nums,target,False)
        return [left,right]

        # Method
        # 1、首先，在 nums 数组中二分查找 target；
        # 2、如果二分查找失败，则 binarySearch 返回 -1，表明 nums 中没有 target。此时，searchRange 直接返回 {-1, -1}；
        # 3、如果二分查找成功，则 binarySearch 返回 nums 中值为 target 的一个下标。然后，通过左右滑动指针，来找到符合题意的区间
        def binarySearch(nums,target):
            left = 0
            right = len(nums)-1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] > target:
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                return mid

        index = binarySearch(nums, target)
        if index == -1: return [-1,-1]
        left,right = index,index
        while left-1 >=0 and nums[left-1]==nums[left]:
            left -=1
        while right < len(nums)-1 and nums[right+1]==nums[right]:
            right += 1
        return [left,right]
