class Solution:
    def candy(self, ratings: list[int]) -> int:
        '''
        两次贪心: 一次是从左到右遍历，只比较右边孩子评分比左边大的情况。一次是从右到左遍历，只比较左边孩子评分比右边大的情况。
        '''
        # time O(N) space O(1)
        n = len(ratings)
        res = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                res[i] = max(res[i], res[i + 1] + 1)
        return sum(res)