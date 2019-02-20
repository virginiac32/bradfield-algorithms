# Network delay time Leetcode problem
# https://leetcode.com/problems/network-delay-time/submissions/

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
