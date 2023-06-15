def search(self, nums: list[int], target: int) -> int:
    # [left, right)
    left = 0 
    right = len(nums)
    while left < right:  # when left == right, [left,right) is invalid interval, so use <
        mid = (right+left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1  #  target in right interval [middle + 1, right)
        else:
            right = mid    # target in left interval [left, middle)
    return False 
    
    # [left, right]
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (right+left)//2
        if nums[mid]==target:
            return mid
        elif nums[mid] < target:
            left = mid+1    # target in right interval [middle + 1, right]
        else:
            right = mid-1  # target in left interval [left, middle-1]
