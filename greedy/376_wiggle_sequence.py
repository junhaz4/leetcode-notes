class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        '''
        局部最优：删除单调坡度上的节点（不包括单调坡度两端的节点），那么这个坡度就可以有两个局部峰值。
        整体最优：整个序列有最多的局部峰值，从而达到最长摆动序列。
        实际操作上，其实连删除的操作都不用做，因为题目要求的是最长摆动子序列的长度，所以只需要统计数组的峰值数量就可以了（
        相当于是删除单一坡度上的节点，然后统计长度)这就是贪心所贪的地方，让峰值尽可能的保持峰值，然后删除单一坡度上的节点。
        '''
        # time O(n) space O(1)
        if len(nums) <= 1:
            return len(nums)
        pre_diff = 0
        cur_diff = 1
        res = 1
        for i in range(len(nums) - 1):
            cur_diff = nums[i + 1] - nums[i]
            # if cur_diff * pre_diff <= 0 and cur_diff != 0:
            if (cur_diff > 0 and pre_diff <= 0) or (cur_diff < 0 and pre_diff >= 0):
                res += 1
                pre_diff = cur_diff
        return res

class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        '''
        method 2 DP: use two arrays to store ups and downs
        If nums[i] > nums[i-1]nums[i]>nums[i−1], that means it wiggles up. The element before it must be a down position.
        So up[i] = down[i-1] + 1up[i]=down[i−1]+1, down[i]down[i] remains the same as down[i-1]down[i−1].
        If nums[i] < nums[i-1]nums[i]<nums[i−1], that means it wiggles down. The element before it must be a up position.
        So down[i] = up[i-1] + 1down[i]=up[i−1]+1, up[i]up[i] remains the same as up[i-1]up[i−1].
        If nums[i] == nums[i-1]nums[i]==nums[i−1], that means it will not change anything because it didn't wiggle at all.
        So both down[i]down[i] and up[i]up[i] remain the same as down[i-1]down[i−1] and up[i-1]up[i−1].
        At the end, find the max of the two arrays
        '''
        # time O(n) space O(n)
        if len(nums) < 2:
            return len(nums)
        n = len(nums)
        up = [0]*n
        down = [0]*n
        up[0] = 1
        down[0] = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]: # nums[i] is peak
                up[i] = down[i-1]+1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]: # nums[i] is down
                up[i] = up[i-1]
                down[i] = up[i-1]+1
            else: # nums[i] same as before
                up[i] = up[i-1]
                down[i] = down[i-1]
        return max(up[-1],down[-1])