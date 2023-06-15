def getUanlloatedUsers(bids,total_shares):
    bids.sort(key=lambda x: (-x[2],x[3]))
    i = 0
    res = []
    while total_shares > 0 and i < len(bids):
        id,shares,price,time = bids[i]
        i += 1
        if total_shares < shares:
            total_shares = 0
            break
        total_shares -= shares
    for j in range(i,len(bids)):
        res.append(bids[j][0])
    return res


#$bids = [[1,5,5,0],[2,7,8,1],[3,7,5,1],[4,10,3,3]]
bids = [[1,2,5,0],[2,1,4,2],[3,5,4,6]]
total_shares = 3
#print(getUanlloatedUsers(bids,total_shares))

from collections import deque
class RateLimitAPI:
    def __init__(self,time_window,limit):
        self.window = time_window
        self.limit = limit
        self.used = {}
        self.que = {}

    def rateLimit(self, timestamp, count, user):
        if user not in self.used:
            self.used[user] = 0
            self.que[user] = deque()

        d = self.que[user]
        forgive = timestamp - self.window - 1
        while d and d[0][0] <= forgive:
            self.used[user] -= d.popleft()[1]

        avail = self.limit - self.used[user]
        count = min(count, avail)
        self.used[user] += count
        d.append((timestamp, count))

        return count


'''
ans = [-1]
sites = [90,95,80,85,70]
routes = [[0,4],[1,2],[2,3],[1,0],[0,2],[4,3]]
def dfs(i, num, visited, res):
    visited.add(i)
    if num == 4:
        ans.append(res)
    for neighbour in routes:
        if neighbour not in visited:
            num += 1
            dfs(neighbour,num,visited,res+sites[neighbour])
            num -= 1
    visited.remove(i)
for i in range(len(sites)):
    visited = set()
    dfs(i,1,visited,sites)
'''

def missedAuction(bids, totShares):
    # bids[i] = [id, shares, price, time]
    prices = {}
    for i,s,p,t in bids:
        if p not in prices:
            prices[p] = []
        prices[p].append((t, i, s))

    ret = []
    sp = sorted(prices.keys(), reverse = True)
    for it,p in enumerate(sp):
        ct = len(prices[p])
        # add up the total requested shares by each person at this
        # price requested
        tot = sum(s for _, _, s in prices[p])
        if tot <= totShares:
            totShares -= tot
        else:
            # if we don't have as many shares as we have folks
            # bidding at this price, exactly (ct - totShares)
            # people at this price will not get shares, depending
            # on their timestamps
            if ct > totShares:
                leftOut = ct - totShares
                # sort by timestamp in reverse, the first leftOut
                # people won't get shares as they had the latest
                # submissions
                users = sorted(prices[p], reverse = True)
                for i in range(leftOut):
                    ret.append(users[i][1])

            break

    # everyone we didn't get to in the above iteration will
    # definitely not get any shares because we used them all
    for it2 in range(it + 1, len(sp)):
        for _, bidder, _ in prices[sp[it2]]:
            ret.append(bidder)

    return ret

print(missedAuction([[1,2,5,0],[2,1,4,2],[3,5,4,6]],3))

def ancestor_names(names):
    def roman_to_int(s: str):
        rom_to_int_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sub_map = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        summation = 0
        idx = 0

        while idx < len(s):
            if s[idx:idx + 2] in sub_map:
                summation += sub_map.get(s[idx:idx + 2])
                idx += 2
            else:
                summation += rom_to_int_map.get(s[idx])
                idx += 1
        return summation

    name_array = []
    for name in names:
        n, num = name.split()
        num = roman_to_int(num)
        name_array.append((n, num, name))
    name_array.sort(key=lambda x: [x[0], x[1]])
    return list(map(lambda x: x[2], name_array))
'''
def ancestral_names(arr):
    arr.sort(key = lambda x: (x.split(" ")[0], romanToInt(x.split(" ")[1]) ))
    return arr

def romanToInt(s: str) -> int:
    numerals = {
        "I":1, "V":5, "X":10,
        "L":50, "C":100, "D":500, "M":1000
    }
    output = 0
    for i, c in enumerate(s):
        if i + 1 < len(s) and numerals[c] < numerals[s[i+1]]:
            output -= numerals[c]
        else:
            output += numerals[c]
    return output

names = ["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"]
print(ancestral_names(names))
'''

'''
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer.
Find out what could be the possible minimum difference of the height of shortest and longest towers after you have modified each tower.

Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)

Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as
{3, 3, 6, 8}. The difference between
the largest and the smallest is 8-3 = 5.
'''
class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        maxo = arr[-1]
        mino = arr[0]
        out = maxo-mino
        for i in range(1, n):
            maxo = max(arr[i-1]+k, arr[-1]-k)
            mino = min(arr[i]-k, arr[0]+k)
            out = min(out, maxo-mino)
        return out