class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp[i]表示以nums[i]结尾的最长子序列
        # count[i]表示以nums[i]结尾的最长子序列的个数
        # 那么在nums[i] > nums[j]前提下, (0<=j<i)
            # dp[j]+1 > dp[i]说明找到了以nums[i]的一个更长的子序列，最长递增子序列的长度增加了，dp[i] = dp[j] + 1，长度增加，数量不变第一次找到, count[i] = count[j]
            # dp[j]+1 = dp[i]说明再次找到了以nums[i]结尾的最长子序列，说明最长递增子序列的长度并没有增加，但是出现了长度一样的情况, count[i] + count[j]
        # 初始化，一开始都是1
        # 遍历顺序，两层遍历，i从前往后遍历，j从前往i遍历
        n = len(nums)
        if n <= 1:
            return 1
        dp = [1]*n 
        count = [1]*n 
        res = 0
        max_len = 0
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j]+1 > dp[i]:
                        dp[i] = dp[j]+1
                        count[i] = count[j]
                    elif dp[j]+1 == dp[i]:
                        count[i] += count[j]
                max_len = max(max_len,dp[i])
        
        # 如果dp数组记录的最大长度dp[i]等于max_len，将对应的数量count[i]加到结果res中
        for i in range(n):
            if max_len == dp[i]:
                res += count[i]
        return res 