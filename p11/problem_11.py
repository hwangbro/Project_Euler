import math

filename = 'input.txt'

def main():
	totalf = []
	with open(filename, 'r') as f:
		for line in f:
			totalf.append(line.strip())
	grid = list()
	for line in totalf:
		grid.append([int(i) for i in line.split(' ')])

	h = hmax(grid)
	v = vmax(grid)
	d = dmax(grid)
	m = max([h,v,d])
	print((h,v,d))
	print(m)

def prod(numlist):
	answer = numlist[0]
	for n in numlist[1:]:
		answer *= n
	return answer

def hmax(grid):
	m = 0
	for line in grid:
		for i in range(4, 20):
			x = prod(line[i-4:i])
			if x > m:
				m = x
	return m

def vmax(grid):
	m = 0
	for i in range(20):
		for j in range(4,20):
			a = []
			a.append(grid[j-4][i])
			a.append(grid[j-3][i])
			a.append(grid[j-2][i])
			a.append(grid[j-1][i])
			x = prod(a)
			if x > m:
				m = x
	return m

def dmax(grid):
	m = 0
	for i in range(4,20):
		for j in range(4,20):
			a = []
			a.append(grid[i-4][j-4])
			a.append(grid[i-3][j-3])
			a.append(grid[i-2][j-2])
			a.append(grid[i-1][j-1])
			x = prod(a)
			if x > m:
				m = x
	
	for i in range(3,20):
		for j in range(3,20):
			a = []
			a.append(grid[i-3][j])
			a.append(grid[i-2][j-1])
			a.append(grid[i-1][j-2])
			a.append(grid[i][j-3])
			x = prod(a)
			if x > m:
				m = x

	return m
main()	
