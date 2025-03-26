class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 暴力解法，两层for循环，一层for循环遍历数组，另一组for循环找第一个比当前元素大的元素o(n^2)
        # 单调栈，适合解决寻找任一个元素的右边或者左边第一个比自己大或者小的元素的位置，o(n)
        # 本题就是要找到当前元素右边第一个比当前元素大的元素，使用单调栈记录遍历过的元素
        # 需要注意的是栈内的单调性
            # 递增，寻找的当前元素右边第一个更大的元素, 把尽可能小的元素放在栈口，这样当遍历到一个元素大于栈口元素的时候，当前元素就是右边第一个比栈口元素大的值
            # 递减，寻找的当前元素右边第一个更小的元素
        n = len(temperatures)
        st = [0]
        res = [0]*n
        for i in range(1,n):
            if temperatures[i] <= temperatures[st[-1]]: # 如果当前元素小于等于栈口元素就直接加入，保持栈内递增
                st.append(i)
            else: # 如果当前元素大于栈口元素，说明当前元素是栈口元素右边第一个比它大的，记录res中
                while st and temperatures[i] > temperatures[st[-1]]:
                    index = st.pop()
                    res[index] = i-index
                st.append(i)
        return res