class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        '''
        第一步：将数组按照绝对值大小从大到小排序，注意要按照绝对值的大小
        第二步：从前向后遍历，遇到负数将其变为正数，同时K--
        第三步：如果K还大于0，那么反复转变数值最小的元素，将K用完
        第四步：求和
        '''
        # time O(n*logn) space O(1)
        nums.sort(key=lambda x: abs(x))
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
        if k%2 == 1:
            nums[0] *= -1
        return sum(nums)