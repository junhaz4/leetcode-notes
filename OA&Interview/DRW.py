def minCost(string,cost):
    '''min cost to remove duplicate characters in a string'''
    total_cost = 0
    left, right = 0, 0
    n = len(cost)
    while left < n and right < n:
        cur_total = 0
        cur_max = 0
        while right < n and string[left] == string[right]:
            cur_total += cost[right]
            cur_max = max(cur_max, cost[right])
            right += 1
        left = right
        total_cost += cur_total-cur_max
    return total_cost
'''
    total_cost = 0
    cur_max_cost = 0
    for i in range(len(string)):
        if i > 0 and string[i] != string[i-1]:
            cur_max_cost = 0
        total_cost += min(cur_max_cost,cost[i])
        cur_max_cost = max(cur_max_cost,cost[i])
    return total_cost
'''


def countPronic(A, B):
    '''find the total number of integers can be written as x(x+1) in a given range[A...B]'''
    def pronic(num):
        # Check upto sqrt N
        N = int(num ** (1 / 2))
        # If product of consecutive
        # numbers are less than equal to num
        if (N * (N + 1) <= num):
            return N
        # Return N - 1
        return N - 1
    return pronic(B) - pronic(A - 1)
'''
import math
def checkPronic(x) :
    for i in range(int(math.sqrt(x)) + 1):
        if (x == i * (i + 1)) :
            return True
    return False
def countPronic(A, B) :
    count = 0
    for i in range(A, B + 1):
        if (checkPronic(i) != 0) :
            count += 1
    return count
'''

def smallestNumber(N):
    '''find the smallest number greater than N whose digit sum is twice as big as digit sum of N'''
    def getSum(num):
        digit_sum = 0
        while num:
            digit_sum += num%10
            num = num//10
        return digit_sum
    i = getSum(N)
    d = 2*i
    k = N
    # while k <...
    while k<=500:
        if getSum(k) == d:
            return k
        k += 1
    return -1

import collections
def maxNumNonOverlappingEqaulSum(A):
    '''find the maximum number of non-ovelapping segments of length 2 such that segments have equal sum'''
    res = collections.defaultdict(int, {sum(A[:2]): 1})
    seen = collections.defaultdict(int, {sum(A[:2]): 0})
    for i in range(len(A) - 1):
        val = sum(A[i: i + 2])
        if i >= seen[val] + 2:
            res[val] += 1
            seen[val] = i
    return res[max(res, key=res.get)]

def solution(A):
    def get_count(idx, cur_sum, arr):
        n = len(arr)
        if idx >= n-1:
            return 0
        count = 0
        if arr[idx] + arr[idx+1] == cur_sum:
            count = 1 + get_count(idx+2,cur_sum,arr)
        return max(count,get_count(idx+1,cur_sum,arr))
    n = len(A)
    count = 0
    for i in range(0,n-1):
        cur_sum = A[i]+A[i+1]
        count = max(count,1+get_count(i+2,cur_sum,A))
    return count