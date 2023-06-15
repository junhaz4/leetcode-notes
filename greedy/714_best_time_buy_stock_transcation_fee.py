class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        '''
        本题有了手续费，就要关系什么时候买卖了，因为计算所获得利润，需要考虑买卖利润可能不足以手续费的情况
        所以我们在做收获利润操作的时候其实有三种情况：
        情况一：收获利润的这一天并不是收获利润区间里的最后一天（不是真正的卖出，相当于持有股票），所以后面要继续收获利润。
        情况二：前一天是收获利润区间里的最后一天（相当于真正的卖出了），今天要重新记录最小价格了。
        情况三：不作操作，保持原有状态（买入，卖出，不买不卖）
        '''
        # time O(n) space O(1)
        result = 0
        minPrice = prices[0]  # 记录最低价格
        for i in range(1, len(prices)):
            if prices[i] < minPrice:  # 情况二：相当于买入
                minPrice = prices[i]
            elif prices[i] >= minPrice and prices[i] <= minPrice + fee:  # 情况三：保持原有状态（因为此时买则不便宜，卖则亏本）
                continue
            else: # 计算利润，可能有多次计算利润，最后一次计算利润才是真正意义的卖出
                result += prices[i] - minPrice - fee
                minPrice = prices[i] - fee # 情况一，这一步很关键
        return result
# 从代码中可以看出对情况一的操作，因为如果还在收获利润的区间里，表示并不是真正的卖出，而计算利润每次都要减去手续费，
# 所以要让minPrice = prices[i] - fee;，这样在明天收获利润的时候，才不会多减一次手续费