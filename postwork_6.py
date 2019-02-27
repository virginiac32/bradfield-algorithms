# Triangles problem
# https://leetcode.com/problems/triangle/

def min_triangles_sum(triangle):
	level = len(triangle) - 2
	while level >= 0:
		for index, item in enumerate(triangle[level]):
			triangle[level][index] = item + min(triangle[level + 1][index],
												triangle[level + 1][index + 1])
		level -= 1
	return triangle[0][0]


test_triangle = [[3], [8, 5], [1, 2, 6], [1, 1, 6, 3]]
print(min_triangles_sum(test_triangle))


# Decode ways problem
# https://leetcode.com/problems/decode-ways/

def numDecodings(s):
	if int(s[0]) == 0:
		return 0
	if int(s[0]) != 0 and len(s) == 1:
		return 1
	for i in range(1, len(s)):
		if s[i - 1:i + 1] == '00':
			return 0
	solutions = [None] * len(s)
	solutions[0] = 1
	if len(s) >= 2:
		if int(s[0:1]) == 0:
			solutions[1] = 0
		elif int(s[1:2]) == 0:
			if int(s[0:2]) > 26:
				return 0
			else:
				solutions[1] = 1
		elif int(s[0:2]) <= 26:
			solutions[1] = 2
		else:
			solutions[1] = 1
	if len(s) == 2:
		return solutions[1]
	for i in range(2, len(solutions)):
		last_two_digits = int(s[i - 1:i + 1])
		current_digit = int(s[i:i + 1])
		last_digit = int(s[i - 1:i])
		if last_two_digits <= 26 and current_digit != 0 and last_digit\
			!= 0:
			solutions[i] = solutions[i - 1] + solutions[i - 2]
		if last_two_digits > 26 or last_digit == 0:
			solutions[i] = solutions[i - 1]
		if current_digit == 0:
			if last_two_digits > 26:
				return 0
			else:
				solutions[i] = solutions[i - 2]
	return solutions[-1]

test_code = '226'
print(numDecodings(test_code))


# Coin change problem
# https://leetcode.com/problems/coin-change/

from heapq import heappush, heappop

# this solution was too slow :(
def coinChange(coins, amount):
	coins.sort(reverse=True)
	if amount in coins:
		return 1
	if amount == 0:
		return 0
	if amount < coins[-1]:
		return -1
	queue = []

	for i in coins:
		heappush(queue, (0, 1, i))

	while queue:
		prev_sum, count, current_coin = heappop(queue)
		total = prev_sum + current_coin
		if total == amount:
			return count
		elif total < amount:
			for j in coins[0:coins.index(current_coin) + 1]:
				heappush(queue, (total, count + 1, j))
	return -1

print(coinChange([11,3], 10))