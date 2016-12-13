import math

def main():
	sol = []
	for a in range(1, 500):
		b = a+1
		c = b+1
		while c <= 500:
			while c*c < a*a + b*b:
				c += 1
			if c*c == a*a + b*b and c <= 500 and a+b+c == 1000:
				print((a,b,c))
				print(a*b*c)
				return
			b += 1
	
main() 
