class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # 局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算连续和
        # time: O(n) space O(1)
        if not nums:
            return 0
        cur_sum = 0
        max_sum = float("-inf")
        for n in nums:
            cur_sum += n
            max_sum = max(max_sum,cur_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum