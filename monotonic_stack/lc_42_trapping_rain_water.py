class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针(额外数组)
        n = len(height)
        if n <= 2:
            return 0
        max_left = [0]*n
        max_right = [0]*n
        # 记录每个柱子左边柱子最大高度, 当前元素的左边最高位置是前一个位置的左边最高高度和本高度的最大值
        max_left[0] = height[0]
        for i in range(1,n):
            max_left[i] = max(max_left[i-1],height[i])
        # 记录每个柱子右边柱子最大高度
        max_right[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i])
        # 求和
        res = 0
        for i in range(n):
            water = min(max_left[i],max_right[i])-height[i] # 形成雨水的时候要看的是左右两边高度中较低的那个才能形成洼地
            if water > 0:
                res += water
        return res
    
class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针（不使用额外数组）
        n = len(height)
        if n <= 2:
            return 0
        left_max = 0 # 记录左边最大值
        right_max = 0 # 记录右边最大值
        res = 0
        left, right = 0, n-1
        # while循环可以不加等号，因为在「谁小移动谁」的规则下，相遇的位置一定是最高的柱子，这个柱子是无法接水的。
        while left < right:
            left_max = max(left_max,height[left]) 
            right_max = max(right_max,height[right])
            if left_max < right_max: 
                res += left_max-height[left]
                left += 1
            else:
                res += right_max-height[right]
                right -= 1
        return res 
    
class Solution:
    def trap(self, height: List[int]) -> int:
        # 单调栈（递增）
        # 通过三个元素来接水：栈顶，栈顶的下一个元素，以及即将入栈的元素
        # 雨水高度是 min(凹槽左边高度, 凹槽右边高度) - 凹槽底部高度
        # 雨水的宽度是 凹槽右边的下标 - 凹槽左边的下标 - 1（因为只求中间宽度）
        n = len(height)
        if n <= 2:
            return 0
        st = [0]
        res = 0
        for i in range(1,n):
            # 当前元素高度小于栈口元素高度
            if height[i] < height[st[-1]]:
                st.append(i)
            # 当前柱子高度和栈顶一致时，左边的一个是不可能存放雨水的，所以保留右侧新柱子
            # 需要使用最右边的柱子来计算宽度
            elif height[i] == height[st[-1]]:
                st.pop()
                st.append(i)
            else:
                while st and height[i] > height[st[-1]]:
                    mid_height = height[st.pop()]
                    if st:
                        left_height = height[st[-1]]
                        right_height = height[i]
                        # 两侧的较矮一方的高度 - 凹槽底部高度
                        h = min(left_height,right_height)-mid_height
                        # 凹槽右侧下标 - 凹槽左侧下标 - 1: 只求中间宽度
                        w = i-st[-1]-1
                        # 体积：高乘宽
                        res += h*w
                st.append(i)
        return res 