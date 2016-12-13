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

	print()

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
			a.append(grid[i][j-4])
			a.append(grid[i][j-3])
			a.append(grid[i][j-2])
			a.append(grid[i][j-1])
			x = prod(a)
			if x > m:
				m = x
main()	
