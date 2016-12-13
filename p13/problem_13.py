import math
from decimal import *


filename = 'input.txt'

def main():
	totalf = []
	fl = []
	with open('input.txt', 'r') as f:
		for line in f:
			totalf.append(line.strip())
	for i in range(len(totalf)):
		totalf[i] = totalf[i][:1] + '.' + totalf[i][1:]
		getcontext().prec = 51
		fl.append(Decimal(totalf[i]))

	answer = str(sum(fl))
	print(answer[:3] + answer[4:11])
main()			
