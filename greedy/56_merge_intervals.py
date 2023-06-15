class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        '''
        按照左边界从小到大排序之后，如果 intervals[i][0] <= intervals[i - 1][1] 即intervals[i]左边界 < intervals[i - 1]右边界，
        则一定有重复，因为intervals[i]的左边界一定是大于等于intervals[i - 1]的左边界
        '''
        # time O(nlogn) space O(n)
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        return result
