class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 将nums分成两部分，使得两部分的差值等于target
        # left组合-right组合=target, left组合+right组合=sums， left组合 =（sums+target)/2 
        # 转换成从nums寻找一些数，使得这些数的和为（sums+target)/2, 01背包问题
        # dp[i][j]从[0,i]中选择一些数字，这些数字能组成和为j的数量
        # 递推公式 dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
            # 不用nums[i]，从[0,i-1]中选择一些和为j的数字
            # 用nums[i]，从[0,i-1]中选择和为j-nums[i]的数字
        # 初始化, 需要处理i=0和j=0的情况
        # 从前向后遍历，先遍历数字，再遍历容量

        # 方法一
        total_sum = sum(nums)
        if abs(target) > total_sum or (target+total_sum)%2:
            return 0
        target = (target+total_sum)//2
        n = len(nums)
        dp = [[0]*(target+1) for _ in range(n)]
        # 初始化第一行i=0
        if nums[0] <= target:
            dp[0][nums[0]] = 1
        # 初始化第一列j=0
        zero_count = 0
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
            dp[i][0] = 2**(zero_count)
        '''
        错误初始化，忽略了nums中0的情况
        如果有两个物品，物品0为0， 物品1为0，装满背包容量为0的方法有几种？
        放0件物品、放物品0、放物品1、放物品0和物品1，总共4种方法
        需要统计nums中0的数量，每个0可以取+/-，因此有2的n次方种方法可以取到j=0
        for i in range(n):
            dp[i][0] = 1
        dp[0][nums[0]] = 1
        '''
        for i in range(1,n):
            for j in range(target+1):
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        return dp[n-1][target]
    
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 方法二
        '''
        和方法一不同的是，方法二的dp数组多出了一行，大小为[n+1][target+1]。第0行明确表示。在没有任何元素可用的情况下，和为j的方案数
        初始化逻辑更加清晰，dp[0][0]=1表示在没有任何元素的情况下，和为0的方式有且只有一种，这样就可以避免方法一中初始化0元素带来的问题
        '''
        total_sum = sum(nums)
        if abs(target) > total_sum or (target+total_sum)%2:
            return 0
        target = (target+total_sum)//2
        n = len(nums)
        dp = [[0]*(target+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for j in range(target+1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        return dp[n][target]

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 1维DP
        total_sum = sum(nums)
        if abs(target) > total_sum or (target+total_sum)%2:
            return 0
        target = (target+total_sum)//2
        n = len(nums)
        dp = [0]*(target+1)
        dp[0] = 1 # 当目标和为0时，只有一种方案，即什么都不选
        for n in nums:
            for j in range(target+1,n-1,-1):
                dp[j] = dp[j] + dp[j-n]
        return dp[target]

        