import math


def main():
	n = 40
	k = 20
	answer = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
	print(answer)
main()
