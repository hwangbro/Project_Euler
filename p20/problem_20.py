import math

def main():
	x = long(math.factorial(100))
	a = str(x)
	print(sum([int(i) for i in a]))

main()
