import math
def is_square(n):
    if n >= 0:
        sqrt = int(math.sqrt(n))
        return sqrt*sqrt == n
    return False

def can_reach(c,x1,y1,x2,y2):
    if is_square(x1+x2) or is_square(x2+y2):
        return "No"
    def dfs(x1,y1):
        if is_square(x1+y1):
            return False
        if x1 > x2 or y1 > y2:
            return False
        if x1 == x2:
            if (y2-y1)%x1 == 0 or (y2-y1)%c == 0:
                return True
            else:
                return False
        if y1 == y2:
            if (x2-x1)%y1 == 0 or (x2-x1)%c == 0:
                return True
            else:
                return False
        if x1 == x2 and y1 == y2:
            return True
        return dfs(x1+y1,y1) or dfs(x1,x1+y1) or dfs(x1+c,y1+c)

    if dfs(x1,y1):
        return "Yes"
    return "No"

from collections import deque
def getResult(arrival, street):
    '''
    定义一个基础time
    如果time小于两个queue第一个的时间，说明没有通车
    如果time同时大于两个queue第一个时间，说明遇到conflict，根据之前的条件通车
    如果小于其中一个时间，说明另一台路通车
    '''
    n = len(arrival)
    res = [-1]*n
    time = 0
    prev = -1
    main_street_queue = deque()
    first_avenue_queue = deque()
    for i in range(len(street)):
        if street[i] == 0:
            main_street_queue.append((i,arrival[i]))
        else:
            first_avenue_queue.append((i,arrival[i]))
    while main_street_queue and first_avenue_queue:
        car1 = main_street_queue[0]
        car2 = first_avenue_queue[0]
        if time >= max(car1[1],car2[1]):
            if prev == -1 or prev == 1:
                res[car2[0]] = time
                prev = 1
                first_avenue_queue.popleft()
            else:
                res[car1[0]] = time
                prev = 0
                main_street_queue.popleft()
            time += 1
        else:
            if time >= car1[1]:
                res[car1[0]] - time
                if car2[1] == time+1:
                    prev = 1
                else:
                    prev = -1
                time += 1
                main_street_queue.popleft()
            elif time >= car2[1]:
                res[car2[0]] = time
                if car1[1] == time+1:
                    prev = 0
                else:
                    prev = -1
                time += 1
                first_avenue_queue.popleft()
            else:
                time = min(car1[1],car2[1])
                prev = -1
    while main_street_queue:
        car = main_street_queue[0]
        res[car[0]] = max(time,car[1])
        time = max(time,car[1])+1
        main_street_queue.popleft()
    while first_avenue_queue:
        car = first_avenue_queue[0]
        res[car[0]] = max(time, car[1])
        time = max(time, car[1]) + 1
        first_avenue_queue.popleft()
    return res