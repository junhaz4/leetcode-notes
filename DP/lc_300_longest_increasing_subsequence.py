class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 贪心+二分查找
        # 思路，维护一个递增子序列，为了让序列尽可能的长，每次子序列最后加上的那个数尽可能的小
        # 遍历数组，如果当前元素大于子序列最后一个值，就把它加入到最后
        # 否则找出子序列中比它大的最小值，覆盖掉
        n = len(nums)
        if n <= 1:
            return n 
        tails = [nums[0]]
        for num in nums[1:]:
            if num > tails[-1]:
                tails.append(num)
            else:
                left, right = 0, len(tails)-1
                while left <= right:
                    mid = left + (right-left)//2
                    if tails[mid] < num:
                        left = mid+1
                    else:
                        right = mid-1
                tails[left]=num
        return len(tails)
    
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划
        # dp[i]表示[0,i]区间范围内以nums[i]为结尾的最长子序列
        # 状态转移方程
            # 位置i的最长升序子序列等于j从0到i-1各个位置的最长升序子序列 + 1 的最大值。
            # 注意这里不是要dp[i] 与 dp[j] + 1进行比较，而是我们要取dp[j] + 1的最大值
            # if nums[i]>nums[j] dp[i] = max(dp[i],dp[j]+1)
        # 初始哈，每个位置的大小都是1
        # 从前向后遍历
        n = len(nums)
        if n <= 1:
            return n
        dp = [1]*n 
        res = 1
        for i in range(1,n):
            for j in range(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
            res = max(res,dp[i])
        return res 
        