class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 滑动窗口，想象两把尺子，错开之后比较相同的部分，找最长相同的串
        """
        # 固定nums2，滑动nums1
        nums1: |*|*|*|*|
        nums2: |*|*|*|*|*|*|
                 ↓
        nums1: |*|*|*|*|
        nums2:     |*|*|*|*|*|*|

        # 固定nums1，滑动nums2
        nums1: |*|*|*|*|
        nums2: |*|*|*|*|*|*|
                 ↓
        nums1:       |*|*|*|*|
        nums2: |*|*|*|*|*|*|
        """
        res = 0
        n1, n2 = len(nums1), len(nums2)
        def get_length(i,j):  # 找对齐部分最长相同的串, i指向nums1开始对齐的地方，j指向nums2开始对齐的地方
            nonlocal res 
            cur = 0
            while i < n1 and j < n2:
                if nums1[i] == nums2[j]:
                    cur += 1
                    res = max(cur,res)
                else:
                    cur = 0
                i += 1
                j += 1
            
        for i in range(n1):
            get_length(i,0)
        for j in range(n2):
            get_length(0,j)
        return res 
    

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 动态规划
        # dp[i][j]表示以下标i - 1为结尾的A，和以下标j - 1为结尾的B，最长重复子数组长度为dp[i][j]
        # 递推公式，当A[i - 1] 和B[j - 1]相等的时候，dp[i][j] = dp[i - 1][j - 1] + 1
        # 初始化dp[i][0]和dp[0][j]本身无意义，但为了方便递推初始化为0
        # 从前向后遍历
        n1, n2 = len(nums1), len(nums2)
        res = 0
        dp = [[0]*(n2+1) for _ in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                res = max(res,dp[i][j])

        # 优化空间复杂度
        n1, n2 = len(nums1), len(nums2)
        res = 0
        dp = [0]*(n2+1)
        for i in range(1,n+1):
            for j in range(n2,1,-1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = dp[j-1]+1
                else:
                    dp[j] = 0
                res = max(res,dp[j])
        return res 