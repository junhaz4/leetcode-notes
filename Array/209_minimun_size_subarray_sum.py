'''
Method 1: Brute Force
Two for loops: 是一个for循环滑动窗口的起始位置，一个for循环为滑动窗口的终止位置，用两个for循环 完成了一个不断搜索区间的过程
Time: O(n^2)
Space: O(1)
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        min_length = n + 1
        for i in range(n):
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                if sum >= target:
                    min_length = min(min_length, j - i + 1)
                    break
        return min_length if min_length <= n else 0

'''
Method 2: Sliding Window
窗口内是什么           窗口就是满足其和 ≥ s的长度最小的 连续 子数组。
如何移动窗口的起始位置？ 窗口的起始位置如何移动：如果当前窗口的值大于s了，窗口就要向前移动了（也就是该缩小了）。
如何移动窗口的结束位置？ 窗口的结束位置如何移动：窗口的结束位置就是遍历数组的指针，也就是for循环里的索引。
Time: O(n)
Space: O(1)
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        start = 0
        min_length = n+1
        window = 0
        for end in range(n):
            window += nums[end]
            while window >= target:
                min_length = min(min_length, end-start+1)
                window -= nums[start]
                start += 1
        return min_length if min_length <= n else 0