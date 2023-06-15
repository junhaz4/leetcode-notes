class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        use hashset to store already seen numbers and if a number appears again, return False
        time complexity: O(log n)
        space complexity: O(log n)
        '''
        def get_sum(n): # this takes O(log n) time
            ans = 0
            while n > 0:
                ans += (n % 10) ** 2
                n //= 10
            return ans

        seen = set()
        while True:
            n = get_sum(n)
            if n == 1:
                return True
            if n in seen:
                return False
            else:
                seen.add(n)

class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        treat it as a cycle finding problem with floyd cycle finding algorithm (slow, fast pointers)
        if the number is a happy number, there is no cycle in the number.
        if not, the fast and slow pointers will eventually meet
        time complexity: O(log n)
        space complexity: O(1)
        '''
        def get_next(n):
            ans = 0
            while n > 0:
                ans += (n % 10) ** 2
                n //= 10
            return ans
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1