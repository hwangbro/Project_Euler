import math

filename = 'input.txt'

def main():
	totalf = []
	fl = []
	with open('input.txt', 'r') as f:
		for line in f:
			totalf.append(line.strip())
	for i in range(len(totalf)):
		totalf[i] = totalf[i][:1] + '.' + totalf[i][1:]
		fl.append(float(totalf[i]))

	for i in fl:
		print(i)


main()			
