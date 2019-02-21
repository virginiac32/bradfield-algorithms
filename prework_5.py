# Network delay time Leetcode problem
# https://leetcode.com/problems/network-delay-time/submissions/
# My solution didn't work because it utilized Djikstra's in the reading,
# which was incorrect because if you change an item in a Python queue it won't
# update the position of it in the queue

class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """

        distances = {vertex: float('infinity') for vertex in range(1,N+1)}
        distances[K] = 0

        entry_lookup = {}
        pq = []

        for vertex, distance in distances.items():
            entry = [distance, vertex]
            entry_lookup[vertex] = entry
            heapq.heappush(pq, entry)

        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)

            neighbors = [tuples[1:3] for tuples in times if tuples[0] == current_vertex]

            for neighbor, neighbor_distance in neighbors:
                distance = distances[current_vertex] + neighbor_distance
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    entry_lookup[neighbor][0] = distance

        if any(distance == float('infinity') for distance in distances.values()):
            return -1

        return max(distances.values())


# Doing in class together
# May not be totally right

from collections import defaultdict
from heapq import heappush, heappop

INF = float('infinity')

def networkDelayTime(self, times, N, K):
    graph = defaultdict(list)
    for (u,v,w) in times:
        graph[u].append((v,w))

    pq = [(0, K)]
    distances = {}
    for i in range(1, N+1):
        distances[i] = INF
    distances[K] = 0
    while pq:
        d, node = heappop(q)
        if node in distances and distances[node] < d:
            continue
        for neighbor, weight in graph[node]:
            if distances
            heappush(pq, (d + weight, neighbor))
            distances[neighbor] = d + weight

    result = 0
    for node in range(1, N+1):
        if node not in distances:
            return -1
        result = max(result, distances[node])
    return result