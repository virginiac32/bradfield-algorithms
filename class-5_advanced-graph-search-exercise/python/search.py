from collections import deque
from heapq import heappush, heappop
from constants import *

def bfs(grid, start, goal):
  explored = {}
  explored[start] = None
  queue = deque([start])
  while queue:
    node = queue.popleft()
    children = possible_children(node, len(grid[0])-1, len(grid)-1)
    for child in children:
      if child == goal:
        explored[child] = node
        return explored
      elif not child in explored and grid[child[0]][child[1]] != M:
        explored[child] = node
        queue.append(child)
  return explored

def dfs(grid, start, goal):
  explored = {}

  def traverse(node, parent):
    explored[node] = parent
    children = possible_children(node, len(grid[0])-1, len(grid)-1)
    for child in children:
      if child == goal:
        explored[child] = node
        return explored
      if child not in explored and grid[child[0]][child[1]] != M:
        traverse(child, node)

  traverse(start, None)
  return explored

def ucs(grid, start, goal):
  explored = {}
  explored[start] = None
  queue = [(0, start)]

  while queue:
    distance, node = heappop(queue)
    children = possible_children(node, len(grid[0])-1, len(grid)-1)
    for child in children:
      if child == goal:
        explored[child] = node
        return explored
      elif not child in explored and grid[child[0]][child[1]] != M:
        explored[child] = node
        heappush(queue, (distance + COSTS[grid[child[0]][child[
          1]]], child))
  return explored

def a_star(grid, start, goal):
  explored = {}
  explored[start] = None
  queue = [(0, start)]

  while queue:
    distance, node = heappop(queue)
    children = possible_children(node, len(grid[0])-1, len(grid)-1)
    for child in children:
      if child == goal:
        explored[child] = node
        return explored
      elif not child in explored and grid[child[0]][child[1]] != M:
        explored[child] = node
        heappush(queue, (distance + COSTS[grid[child[0]][child[
          1]]] + heuristic(goal, child), child))
  return explored

def heuristic(goal, next):
  return abs(goal[0]-next[0]) + abs(goal[1]-next[1])

def possible_children(parent, max_row, max_col):
  operations = [(-1,0), (0,-1), (1,0), (0,1)]
  children = []
  for operation in operations:
    tuple = (parent[0]+operation[0], parent[1]+operation[1])
    if 0 <= tuple[0] <= max_row and 0 <= tuple[1] <= max_col:
      children.append(tuple)
  return children