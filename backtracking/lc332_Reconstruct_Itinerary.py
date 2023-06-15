class Solution:
    def findItinerary(self, tickets: list[list[str]]):
        from collections import defaultdict
        ticket_map = defaultdict(list)
        for ticket in tickets:
            depart, destination = ticket[0],ticket[1]
            ticket_map[depart].append(destination)
        '''
        tickets_dict里面的内容是这样的
         {'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        '''
        path =["JFK"]
        def backtracking(start):
            if len(path) == len(tickets)+1:
                return True
            ticket_map[start].sort()
            for _ in ticket_map[start]:
                #必须及时删除，避免出现死循环
                end = ticket_map[start].pop(0)
                path.append(end)
                # 只要找到一个就可以返回了
                if backtracking(end):
                    return True
                path.pop()
                ticket_map[start].append(end)
        backtracking("JFK")
        return path