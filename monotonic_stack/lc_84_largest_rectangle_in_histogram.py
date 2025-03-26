class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
         # 暴力解法O(n^2)，遍历heights，以每一根柱子为主心骨（当前轮最高的参照物），直到左侧和右侧各第一个高度矮的柱子
         # 示例1，5左边第一个矮的是1，说明5无法往左边扩展，5右边第一个矮的是2，说明5可以往6柱子扩展，这样就得到了以5柱子作为高度的矩形的宽度和面积，重复此过程直到遍历结束
        res = 0
        n = len(heights)
        for i in range(n):
            left, right = i, i 
            for _ in range(left,-1,-1):
                if heights[left] < heights[i]:
                    break 
                left -= 1
            for _ in range(right,n):
                if heights[right] < heights[i]:
                    break 
                right += 1
            width = right-left-1
            height = heights[i]
            res = max(res,width*height)
        return res 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 双指针
        n = len(heights)
        left_min = [0]*n 
        right_min = [0]*n
        res = 0

        # 记录每个柱子的左侧第一个矮一级的柱子的下标
        left_min[0] = -1
        for i in range(1,n):
            # 向左寻找比当前柱子的第的第一个柱子
            temp = i-1
            while temp >= 0 and heights[temp] >= heights[i]:
                # 当当前柱子的左侧柱子较高时，尝试这个高柱子的left_min值
                temp = left_min[temp]
            left_min[i] = temp

        # 记录每个柱子的右侧第一个矮一级的柱子的下标
        right_min[n-1] = n
        for i in range(n-2,-1,-1):
            temp = i+1
            while temp < n and heights[temp] >= heights[i]:
                temp = right_min[temp]
            right_min[i] = temp
        
        # 计算每一个柱子能形成的面积
        for i in range(n):
            height = heights[i]
            width = right_min[i]-left_min[i]-1
            area = height*width
            res = max(res,area)
        return res

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈（递减，因为要求左右第一个小的）
        # 如果数组本身就是单调递增的，那么在栈内就是单调递减的，无法触发栈内元素弹出的计算，需要在尾部增加一个0
        # 如果数组本身就是单调递减的，那么栈内就只会有1个元素，同样无法计算，所以需要在头部加入一个0
        heights = [0]+heights+[0]
        n = len(heights)
        st = [0]
        res = 0
        for i in range(1,n):
            while st and heights[i] < heights[st[-1]]:
                mid_index = st.pop()
                if st:
                    left_index = st[-1]
                    right_index = i
                    width = right_index-left_index-1
                    height = heights[mid_index]
                    res = max(res,width*height)
            st.append(i)
        return res 