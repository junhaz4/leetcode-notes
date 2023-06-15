# Note: 数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖

'''
Method 1: slow fast pointer 快慢指针法
fast：search for elements of new array where new array contains not target vaule 寻找新数组的元素 ，新数组就是不含有目标元素的数组
slow：points to the index of updated new array 指向更新 新数组下标的位置
Time: O(n)
Space: O(1)
'''
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow

'''
Method 2: two pointers 相向双指针方法
left: find the index of element=val from left 从左向右寻找等于目标值的位置
right: find the index of element!=val from right从右向左寻找不等于目标值的位置
swap left and right 每次找到一个用不等于的覆盖等于的
Time: O(n)
Space: O(1)
'''
class Solution:
    def removeElement(self, nums, val):
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            while left <= right and nums[right] == val:
                right -= 1
            if left < right:
                nums[left] = nums[right]
                left += 1
                right -= 1
        return left