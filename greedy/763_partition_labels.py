class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        '''
        遍历的过程中相当于是要找每一个字母的边界，如果找到之前遍历过的所有字母的最远边界，说明这个边界就是分割点
        统计每一个字符最后出现的位置 从头遍历字符，并更新字符的最远出现下标，如果找到字符最远出现位置下标和当前下标相等了，则找到了分割点
        '''
        # time O(n), space O(1)
        if not s:
            return []
        result = []
        left, right = 0, 0
        hash_table = [0]*26
        for i in range(len(s)):
            hash_table[ord(s[i])-ord('a')] = i
        for i in range(len(s)):
            right = max(right,hash_table[ord(s[i])-ord('a')])
            if i == right: # 找到一个边界
                result.append(right-left+1)
                left = i + 1 # 更新left位置，从剩下的里面继续找分割点
        return result