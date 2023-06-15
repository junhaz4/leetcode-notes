class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        '''
        首先如果总油量减去总消耗大于等于零那么一定可以跑完一圈，说明 各个站点的加油站 剩油量rest[i]相加一定是大于等于零的。
        每个加油站的剩余量rest[i]为gas[i] - cost[i]。
        i从0开始累加rest[i]，和记为curSum，一旦curSum小于零，说明[0, i]区间都不能作为起始位置，起始位置从i+1算起，再从0计算curSum。
        那么局部最优：当前累加rest[j]的和curSum一旦小于0，起始位置至少要是j+1，因为从j开始一定不行。全局最优：找到可以跑一圈的起始位置
        '''
        # time O(n) space O(1)
        start = 0
        cur_sum, total = 0, 0
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cur_sum < 0:
                start = i + 1
                cur_sum = 0
        if total < 0:
            return -1
        return start

'''
method 2
直接从全局进行贪心选择，情况如下：
情况一：如果gas的总和小于cost总和，那么无论从哪里出发，一定是跑不了一圈的
情况二：rest[i] = gas[i]-cost[i]为一天剩下的油，i从0开始计算累加到最后一站，如果累加没有出现负数，说明从0出发，油就没有断过，那么0就是起点。
情况三：如果累加的最小值是负数，汽车就要从非0节点出发，从后向前，看哪个节点能这个负数填平，能把这个负数填平的节点就是出发节点。
'''
# time O(n) space O(1)
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        cur_sum = 0
        min_sum = float('inf')

        for i in range(n):
            cur_sum += gas[i] - cost[i]
            min_sum = min(min_sum, cur_sum)

        if cur_sum < 0: return -1
        if min_sum >= 0: return 0

        for j in range(n - 1, 0, -1):
            min_sum += gas[j] - cost[j]
            if min_sum >= 0:
                return j

        return -1