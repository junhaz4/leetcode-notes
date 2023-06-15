
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        '''
        切割问题类似组合问题。例如对于字符串abcdef：
        组合问题：选取一个a之后，在bcdef中再去选取第二个，选取b之后在cdef中在选组第三个.....。
        切割问题：切割一个a之后，在bcdef中再去切割第二段，切割b之后在cdef中在切割第三段.....。
        eg s = 'aab'
                                        a    a    b
                                       /     |     \
                                     a|ab   aa|b   aab not palindrome
                                    /   \     |        
                                a|a|b  a|ab|  aa|b|
                                  |      |    check
                                a|a|b|  not palindrome
                                check
                            result = [["a","a","b"],["aa","b"]]
        '''
        self.result = []
        self.path = []
        def backtracking(s,startIndex):
            if startIndex >= len(s):
                self.result.append(self.path[:])
                return 
            for i in range(startIndex,len(s)):
                # check if the substring is a palindrome
                substring = s[startIndex:i+1]
                if substring == substring[::-1]:
                # could also define a function to check palindrome
                #if is_palindrome(s,startIndex,i):
                    self.path.append(substring)
                    backtracking(s,i+1)
                    self.path.pop()
                else:
                    continue
        def is_palindrome(s,start,end):
            i = start
            j = end
            while i<j:
                if s[i]!=s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        backtracking(s,0)
        return self.result
        