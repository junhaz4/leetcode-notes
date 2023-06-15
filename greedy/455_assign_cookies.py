class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        # method 1: 这里的局部最优就是大饼干喂给胃口大的，充分利用饼干尺寸喂饱一个，全局最优就是喂饱尽可能多的小孩。
        # time O(nlogn) space O(1)
        g.sort()
        s.sort()
        idx = len(s)-1
        res = 0
        for i in range(len(g)-1,-1,-1):
            if idx >= 0 and g[i] <= s[idx]:
                res += 1
                idx -= 1
        return res

class Solution:
    # method 2：优先考虑饼干, 小饼干先喂饱小胃口
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        res = 0
        for i in range(len(s)):
            if res <len(g) and s[i] >= g[res]:  #小饼干先喂饱小胃口
                res += 1
        return res