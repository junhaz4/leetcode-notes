import collections
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        # Method 1 backtracking + greedy
        flights = collections.defaultdict(list)
        for depart, arrival in tickets:
            flights[depart].append(arrival)
        itinerary = ["JFK"]
        def backtracking(flight):
            if len(itinerary) == len(tickets)+1:
                return True
            flights[flight].sort()

            for _ in flights[flight]:
                next_flight = flights[flight].pop(0)
                itinerary.append(next_flight)
                if backtracking(next_flight):
                    return True
                itinerary.pop()
                flights[flight].append(flight)
            '''
            for next_flight in flights[flight]:
                itinerary.append(next_flight)
                flights[flight].remove(next_flight)
                if backtracking(next_flight):
                    return True
                flights[flight].append(next_flight)
                flights[flight].sort()
                itinerary.pop()
            '''

        backtracking("JFK")
        return itinerary

# Method 2 Eulerian Cycle
def findItinerary(tickets: list[list[str]]) ->list[str]:
    flights = collections.defaultdict(list)
    for depart, arrival in tickets:
        flights[depart].append(arrival)
    itinerary = []

    def dfs(flight):
        dest = flights[flight]
        # sort in the reverse order since the point we got stuck should be the
        # last airport that we visited and then we follow the visited backwards
        dest.sort(reverse=True)
        while dest:
            # while we visit the edge, we trim it off from graph.
            next_flight = dest.pop(0)
            dfs(next_flight)
        itinerary.append(flight)

    dfs("JFK")
    return itinerary[::-1]