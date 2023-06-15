class Solution:
    def canJump(self, nums: list[int]) -> bool:
        # 转化为可以跳跃的覆盖范围是否能覆盖到终点
        # 贪心算法局部最优解：每次取最大跳跃步数（取最大覆盖范围），整体最优解：最后得到整体最大覆盖范围，看是否能到终点。
        # time O(n) space O(1)
        cover = 0
        i = 0
        while i <= cover: # Python无动态修改for loop变量功能，使用while loop
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1: return True
            i += 1
        return False