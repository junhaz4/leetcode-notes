from collections import defaultdict, deque
def change_currency(string,original,target):
    if not string or not original or not target:
        return -1
    graph = defaultdict(dict)
    originals = []
    targets = []
    for r in string.split(";"):
        #print(r)
        ori,exc,rate = r.split(',')
        #print(ori,exc,rate)
        graph[ori][exc] = float(rate)
        originals.append(ori)
        targets.append(exc)
        #graph[exc][ori] = 1/float(rate)

    res = []
    #seen = set()
    if original not in originals or target not in targets:
        return -1
    def backtracking(cur,val):
        if cur == target:
            res.append(val)
        #seen.add(cur)
        for adj, adj_val in graph[cur].items():
            backtracking(adj,val*adj_val)

    backtracking(original,1)
    return max(res)



string="USD,CAD,1.3;USD,GBP,0.71;USD,JPY,109;GBP,JPY,155"
original ="USA"
target = "JPY"
#print(change_currency(string,original,target))


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
