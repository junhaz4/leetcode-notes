"""
Brute force: iterate through the array and find the max in each window.
Let N - the length of the array, the number of windows is N - k + 1.
Time complexity: O(N * k)
Space complexity: O(N)
"""

from collections import deque
class MyQueue:  # 单调队列从大到小
    def __init__(self):
        self.que = deque()

    def pop(self, value):
        '''
        # 每次弹出的时候，比较当前要弹出的数值是否等于队列出口元素的数值，如果相等则弹出。
        # 同时pop之前判断队列当前是否为空。
        '''
        if self.que and value == self.que[0]:
            self.que.popleft()

    def push(self, value):
        '''
        # 如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为
        # 止, 这样就保持了队列里的数值是单调从大到小的了。
        '''
        while self.que and value > self.que[-1]:
            self.que.pop()
        self.que.append(value)

    def front(self):
        return self.que[0]


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # time complexity: o(N) since each element is only pushed or popped once.
        # space complexity: o(N)
        que = MyQueue()
        res = []
        for i in range(k):  # 先将前k的元素放进队列
            que.push(nums[i])
        res.append(que.front())  # result 记录前k的元素的最大值
        for i in range(k, len(nums)):
            que.pop(nums[i - k])  # 滑动窗口移除最前面元素
            que.push(nums[i])  # 滑动窗口前加入最后面的元素
            res.append(que.front())  # 记录对应的最大值
        return res

# method 2 DP
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        left, right = [0] * n, [0] * n
        left[0] = nums[0]
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            j = n - i - 1
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])
        res = []
        for i in range(n - k + 1):
            res.append(max(left[i + k - 1], right[i]))
        return res
