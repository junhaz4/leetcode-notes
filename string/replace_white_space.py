"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1： 输入：s = "We are happy."
输出："We%20are%20happy."

首先扩充数组到每个空格替换成"%20"之后的大小。
然后从后向前替换空格，也就是双指针法
i指向新长度的末尾，j指向旧长度的末尾
从前向后填充就是O(n^2)的算法了，因为每次添加元素都要将添加元素之后的所有元素向后移动。
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        counter = s.count(' ')
        res = list(s)
        res.extend([' ']*counter*2)
        left, right = len(s)-1, len(res)-1
        while left >= 0:
            if s[left] != ' ':
                s[right] = s[left]
                right -= 1
            else:
                res[right-2:right+1] = '%20'
                right -= 3
            left -= 1
        return ''.join(res)
s

