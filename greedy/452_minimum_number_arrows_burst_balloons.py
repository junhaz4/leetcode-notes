class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        '''
        按照起始位置排序，那么就从前向后遍历气球数组，靠左尽可能让气球重复,如果气球重叠了，重叠气球中右边边界的最小值之前的区间一定需要一个弓箭。
        '''
        # time O(nlog n) space O(1)
        if not points:
            return 0
        points.sort(key=lambda x: x[0])
        result = 1
        for i in range(1,len(points)):
            if points[i][0] > points[i-1][1]: # 气球i和气球i-1不挨着，注意这里不是>=
                result += 1
            else:
                points[i][1] = min(points[i-1][1],points[i][1]) # 更新重叠气球最小右边界
        return result