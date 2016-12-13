import math

def main():
	s = str(long(math.pow(2,1000)))
	print(sum([int(i) for i in s]))

main()
