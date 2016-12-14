import math

filename = 'p8_input.txt'

def main():
	totalf = []
	with open(filename, 'r') as f:
		for line in f:
			totalf.append(line)
	
	allnum = []
	for line in totalf:
		allnum += [int(i) for i in line.strip()]
	
	index = 13
	m = 0
	while index < 1001:
		prod = allnum[index-13:index]
		currmax = prod[0]
		for num in prod[1:]:
			currmax *= num
		if currmax > m:
			m = currmax
		index += 1
		print('index is ' + str(index))
	print(m)
main()	
