class Solution:
    def jump(self, nums: list[int]) -> int:
        # 以最小步数增加最大覆盖范围，如果到达最大覆盖范围还未到终点，步数增加
        # 统计当前最大覆盖范围和下一步最大覆盖范围
        # time O(N) space O(1)
        if len(nums) == 1:
            return 0
        res = 0
        curDistance = 0
        nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(i + nums[i], nextDistance)
            if i == curDistance:
                if curDistance != len(nums) - 1:
                    res += 1
                    curDistance = nextDistance
                    if nextDistance >= len(nums) - 1:
                        break
                else:
                    break
        return res

# method 2 optimized
# 让移动下标，最大只能移动到nums.size - 2的地方就可以, 因为当移动下标指向nums.size - 2时：
# 1. 如果移动下标等于当前覆盖最大距离下标， 需要再走一步（即ans++），因为最后一步一定是可以到的终点。（题目假设总是可以到达数组的最后一个位置）
# 2. 如果移动下标不等于当前覆盖最大距离下标，说明当前覆盖最远距离就可以直接达到终点了，不需要再走一步
class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        jumps = 0
        current_jump_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            # we continuously find how far we can reach in the current jump
            farthest = max(farthest, i + nums[i])
            # if we have come to the end of the current jump,
            # we need to make another jump
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
        return jumps