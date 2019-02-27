# Dynamic programming prework

# A - Frog 1
# https://atcoder.jp/contests/dp/tasks/dp_a

# recursively
def frog(list):
  if len(list) == 1:
    return 0
  if len(list) == 2:
    return abs(list[0]-list[1])
  return min(abs(list[0]-list[1])+frog(list[1:]), abs(list[0]-list[2])+frog(
    list[2:]))


# H - Grid 1
# https://atcoder.jp/contests/dp/tasks/dp_h
