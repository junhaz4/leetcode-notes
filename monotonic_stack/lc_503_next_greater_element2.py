class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 单调栈
        # 方法一，拼接2个nums
        n = len(nums)
        res = [-1]*n 
        st = []
        for i in range(n*2):
            while st and nums[st[-1]] < nums[i%n]:
                index = st.pop()
                res[index] = nums[i%n]
            st.append(i%n)
        return res 
    
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 方法二，遍历两次nums2
        n = len(nums)
        res = [-1]*n 
        st = []
        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                index = st.pop()
                res[index] = nums[i]
            st.append(i)
        #此时stack仍有剩余，有部分数‘无下一个更大元素’待修正
        for i in range(n):
            # 一旦stack为空，就表明所有数都有下一个更大元素，可以返回结果    
            if not st:
                return res 
            while st and nums[st[-1]] < nums[i]:
                index = st.pop()
                res[index] = nums[i]
             #不要将已经有下一个更大元素的数加入栈，这样会重复赋值，只需对第一次遍历剩余的数再尝试寻找下一个更大元素即可
        return res 