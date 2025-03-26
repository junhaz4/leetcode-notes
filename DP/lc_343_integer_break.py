class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i]=将n分层i个数字的积
        # dp[i] = j*(i-j) 或者j*dp[i-j]
        # j*(i-j)是单纯的把整数拆分为两个数相乘，而j*dp[i-j]是拆分成两个以及两个以上的个数相乘。
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3,n+1):
            # 优化：拆分一个数n使之乘积最大，那么一定是拆分成m个近似相同的子数相乘才是最大的
            # 那么 j 遍历，只需要遍历到 n/2 就可以，后面就没有必要遍历了，一定不是最大值。
            for j in range(1,i//2+1):
            #for j in range(1,i-1):
                dp[i] = max(dp[i],j*(i-j),j*dp[i-j])
        return dp[-1]