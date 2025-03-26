class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 单调栈
        n = len(nums1)
        res = [-1]*n
        hashmap = {}
        st = []
        for i in range(n):
            hashmap[nums1[i]] = i 
        for i in range(len(nums2)):
            while st and nums2[st[-1]] < nums2[i]:
                index = st.pop()
                if nums2[index] in hashmap:
                    res[hashmap[nums2[index]]] = nums2[i]
            st.append(i)
        return res