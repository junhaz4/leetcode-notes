class Solution:
    def fourSumCount(self, nums1: list[int], nums2:list[int], nums3: list[int], nums4: list[int]) -> int:
        '''
        这道题目是四个独立的数组，只要找到A[i] + B[j] + C[k] + D[l] = 0就可以，不用考虑有重复的四个元素相加等于0的情况
        1. a hashmap to store (a + b) as key and count as value
        2. iterate through A and B to fill up the hashmap
        3. iterate through C and D, if find 0-(c+d) exists in the hashmap, increment the count store in the hashmap
        time complexity: O(n^2)
        space complexity: O(n^2) there could be n^2 distinct pairs in the hashmap
        '''
        two_sum = {}
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in two_sum:
                    two_sum[n1 + n2] += 1
                else:
                    two_sum[n1 + n2] = 1
        count = 0
        for n3 in nums3:
            for n4 in nums4:
                complement = -(n3 + n4)
                if complement in two_sum:
                    count += two_sum[complement]
        return count
