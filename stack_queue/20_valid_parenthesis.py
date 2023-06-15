class Solution:
    def isValid(self, s: str) -> bool:
        """
        匹配问题都是栈的强项
        第一种情况：已经遍历完了字符串，但是栈不为空，说明有相应的左括号没有右括号来匹配，所以return false
        第二种情况：遍历字符串匹配的过程中，发现栈里没有要匹配的字符。所以return false
        第三种情况：遍历字符串匹配的过程中，栈已经为空了，没有匹配的字符了，说明右括号没有找到对应的左括号return false
        字符串遍历完之后，栈是空的，就说明全都匹配了。
        time complexity: O(n)
        space complexity: O(n)
        """
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif not stack or stack.pop() != char:
                return False
        return not stack