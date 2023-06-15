class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        '''
        局部最优：遇到strNum[i - 1] > strNum[i]的情况，让strNum[i - 1]--，然后strNum[i]给为9，可以保证这两位变成最大单调递增整数。
        从后向前遍历, 就可以重复利用上次比较得出的结果
        '''
        # time O(n) space O(n)
        if n == 0:
            return 0
        a = list(str(n))
        for i in range(len(a)-1,0,-1):
            if int(a[i]) < int(a[i-1]):
                a[i-1] = str(int(a[i-1]) - 1)
                a[i:] = '9' * (len(a) - i)  #python不需要设置flag值，直接按长度给9就好了
        return int("".join(a))