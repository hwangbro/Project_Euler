import math

def collats(sequence, count=1):
	current = sequence[-1]
	if current == 1:
		return (sequence, count)
	elif current % 2 == 0:
		sequence.append(current/2)
	else:
		sequence.append(3*current + 1)
	count+= 1
	return (collats(sequence, count))
	

def main():
	m = 0
	for i in range(1,1000000):
		seq,count = collats([i])
		start = seq[0]
		if count > m:
			m = count
			s = start
#		if i % 10000 == 0:
			#print(i)

	print(s)
main()
