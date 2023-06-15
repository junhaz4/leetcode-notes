from heapq import *
#从小到大排就是小顶堆 min heap，从大到小排就是大顶堆 max heap
# 堆是一棵完全二叉树，树中每个结点的值都不小于（或不大于）其左右孩子的值。 如果父亲结点是大于等于左右孩子就是大顶堆，小于等于左右孩子就是小顶堆。
# method 1 using max_heap
# time complexity: O(K logN)  if k < N O(N) in the particular case of N = k
# space complexity: O(N+k) store the hashmap with no more than N elements and a heap with k elements
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_num = {}
        for n in nums:
            freq_num[n] = freq_num.get(n,0)+1
        max_heap = []
        for num, freq in freq_num.items():
            heappush(max_heap, (-freq,num))
        res = []
        while k:
            k -= 1
            freq, num = heappop(max_heap)
            res.append(num)
        return res

# Method2 using min_heap
# time complexity: O(NlogK)
# space complexity: O(N+k)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_num = {}
        for n in nums:
            freq_num[n] = freq_num.get(n, 0) + 1
        min_heap = []
        for num, freq in freq_num.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heappop(min_heap)[1]
        return result