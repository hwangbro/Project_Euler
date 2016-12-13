import math

def divisors(n):
	ans = [1]
	for i in range(2,int(math.sqrt(n))+1):
		if n % i == 0:
			ans.append(i)
			ans.append(int(n/i))

	ans.append(n)
		
	return sorted(ans)

def tnumb(n):
	count = 0
	for i in range(n+1):
		count += i
	return count

def main():
	count = 1
	div = 0
	while (True):
		numb = tnumb(count)
		d = divisors(numb)
		count += 1
		if len(d) > div:
			div = len(d)
			print((numb,div))
		if len(d) > 500:
			return numb
main()		
