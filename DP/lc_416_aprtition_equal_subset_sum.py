class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 从nums中找到一些数字，使得这些数字的和等于sum(nums)的一半
        # ->01背包问题，从nums中选择一些物品，使得这些物品的容量能够填满容量为sum(nums)/2的背包，这样这些物品的价值(和)也是sum(nums)/2
        # dp[i][j]表示从[0,i]这个区间选择一些数，每个数只能用一次，这些数的和等于j
        # 递推公式：dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
            # dp[i-1][j]（不选i，则从[0，i-1]中选择满足和为j的)
            # dp[i-1][j-nums[i]] （选择i，从[0,i-1]中选择j-nums[i]的)
            # 两者有一个满足条件即可，所以是or
        # 初始化, 要保证递推公式的下标不越界，所以需要对i=0和j=0的情况进行初始化 
        # 遍历顺序，因为dp[i]依赖于dp[i-1]的，所以是从前往后遍历
        sums = sum(nums)
        max_num = max(nums)
        if sums%2 == 1:
            return False 
        target = sums//2
        if max_num > target:
            return False
        n = len(nums)
        dp = [[False]*(target+1) for _ in range(n)]
        dp[0][nums[0]] = True  # 当只取一个数的时候，只有一个正整数nums[0]可以被选取
        for i in range(n): # [0~i]可以取空子集使得和为0
            dp[i][0] = True 
        for i in range(1,n):
            for j in range(target+1):
                if nums[i] > j: # 当前数字大于目标和时，无法使用该数字
                    dp[i][j] = dp[i-1][j]
                else: # 当前数字小于等于目标和时，可以选择使用或不使用该数字
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[n-1][target]
    
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1维DP
        # 在「填表格」的时候，当前行只参考了上一行的值，因此状态数组可以只设置 2 行，使用「滚动数组」的技巧「填表格」即可
        # 实际上，在「滚动数组」的基础上还可以优化，在「填表格」的时候，当前行总是参考了它上面一行 「头顶上」 那个位置和「左上角」某个位置的值。因此，我们可以只开一个一维数组，从后向前依次填表即可
        sums = sum(nums)
        max_num = max(nums)
        if sums%2 == 1:
            return False 
        target = sums//2
        if max_num > target:
            return False
        n = len(nums)
        dp = [False]*(target+1)
        dp[0] = True
        for i in range(n):
            for j in range(target,nums[i]-1,-1):  #到nums[i]的位置停止就行，因为再往下走，就会出现j<nums[i]的情况
                dp[j] = dp[j] or dp[j-nums[i]]
        return dp[target]
