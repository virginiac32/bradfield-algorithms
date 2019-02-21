# Notes
'''
- Impossible curriculum problem:
    - Think of the classes as a graph, with edges as the prereqs
    - If there’s any loop, you know that it’s impossible
        - One edge case - only in a cycle if you revisit a node that’s also
        on your current path
            - So the example of (A > B > D, A > C > D) where A has two
            arrows pointing from it, isn’t considered a cycle. Because you go
            down B > D first, then C > D. And in the 2nd one, you don’t
            consider the first route as part of your current path
￼
- Die hard problem - can make this into weighted graph if the gallons you
transfer is the weights
- Weighted graphs with only 0 and 1 weights
    - Find shorted path from A to B
    - If all the weights were 1, we would treat it as a unweighted graph - BFS
    - If weights include 1 and 0, it’s like BFS, but with a dequeue - if the
    edge is 0, you push to the front of the queue, if it’s 1, you push to the
    back like normal. So when you hit a 0, you use it like a stack (like
    DFS!), and when you hit a 1, you use it like a queue (BFS)
- General non-negative weighted graphs (Dijkstra’s)
    - For negative weighted ones, can you just add the largest neg number to
    all of the weights?
        - Because doing that gives unfair weight to paths that have fewer
        steps (like if one path has two steps with weight 5 vs. another path
        has 5 steps of weight 1), adding a number to each of them would make
        it incorrect
    - We have a region for which we know the shortest paths to every node. So
    at the beginning, the region only includes the starting node  (distance A).
    - Want to grow that region:
        - First find the shortest path that crosses that boundary (the
        current distance plus the weight of the edge that crosses the boundary)
        - When we cross the boundary at the shortest path, we know that we
        have the shortest path to that specific node, because we always
        choose the shortest path node so we know all other possible paths to
        that node will be longer than the one we chose
    - Keep growing the region until everything is in our boundary, then read
    off the shortest paths to get them all
        - You’ll end up with a dictionary of all the nodes with the value
        being the shortest distance to the node
    - To be able to return the actual node paths for the shortest path to a
    node, only need to keep track of each node’s shortest path parent. And
    just keep going back to that node’s parent, etc.
        - Can keep track in a dict of previous = { A: parent }
        - And keep track in a dict of distances = { A: distance }
    - Use priority queue to keep the lowest distance one at the front
        - Put in the priority queue: (node, total distance to node)
            - So could have (F, 4), (F, 5) - and (F, 4) would bubble to the
            front
- Python’s priority queues: if you change an item in the queue it won’t
update the position of it
    - So the way the textbook implemented Djikstra's has an error
- Another way to solve the impossible curriculum problem:
    - Iterative instead of recursive
        - For each node, keep track of its indegree (# of incoming edges)
        - Keep a queue of nodes with 0 indegree
        - Take the first one in the queue, and decrement the indegree of all
        its children, and keep adding to the queue all the nodes with 0 indegree
        - It’s impossible if you have stuff left that still has indegrees left
    - Above approach is called topological sorting: directed acyclical (no
    cycles) graph
        - Result: orders the vertices so that prereqs always come first
        - The order that the nodes come off of the 0 queue is the sort order
'''


# Weighted graphs with on 0 and 1 weights

def shortest_path(s, t):
  # Like BFS, but if you see edges that are 0, you put them on the front of
  # the queue (use a deque). Because you process it immediately the distances in
  # the queue will be groupings of increasing distance - with just X distance
  # and X+1 distances being the *only* ones that can be in the queue.
  # Adding to the beginning of the queue is like using it like a stack - so
  # it's like
  # we're doing DFS when we hit zeros and BFS when we hit ones!

  q = deque()
  q.push_back((s, 0))
  visited = {}
  while q:
    node, d = q.dequeue()
    if node == t:
      return d
    for neighbor, weight in neighbors(node):
      if not visited[neighbor]:
        visited[neighbor] = True
        if weight == 0:
          q.push_front((neighbor, d))
        else:
          q.push_back((neighbor, d + 1))
  return -1
