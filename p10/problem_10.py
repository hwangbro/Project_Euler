import math

def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    i = 2
    while (i <= math.sqrt(x)):
        if (x % i  == 0):
            return False
        i+= 1
    return True

def main():
	a = []
	for i in range(2000000):
		if is_prime(i):
			a.append(i)
		if i % 10000 == 0:
			print(i)
	print(sum(a))
main()
