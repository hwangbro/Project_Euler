import math


def translate_ones(n):
	return {
		0:'',
		1:'one',
		2:'two',
		3:'three',
		4:'four',
		5:'five',
		6:'six',
		7:'seven',
		8:'eight',
		9:'nine'}.get(n)

def translate_tens(n):
	return {
		10:'ten',
		11:'eleven',
		12:'twelve',
		13:'thirteen',
		14:'fourteen',
		15:'fifteen',
		16:'sixteen',
		17:'seventeen',
		18:'eighteen',
		19:'nineteen'}.get(n)

def translate_tens_digit(n):
	t = int(n/10)
	return {
		0:translate_ones(n%10),
		1:translate_tens(n),
		2:'twenty'+translate_ones(n%10),
		3:'thirty'+translate_ones(n%10),
		4:'forty'+translate_ones(n%10),
		5:'fifty'+translate_ones(n%10),
		6:'sixty'+translate_ones(n%10),
		7:'seventy'+translate_ones(n%10),
		8:'eighty'+translate_ones(n%10),
		9:'ninety'+translate_ones(n%10)}.get(t)

def translate_hund_digit(n):
	h = int(n/100)
	t = n%100
	a = 'and'
	if t == 0:
		a = ''
	return ( translate_ones(h) + 'hundred'+a+translate_tens_digit(t))

def pick_number(n):
	if n < 10:
		return translate_ones(n)
	elif n < 20:
		return translate_tens(n)
	elif n < 100:
		return translate_tens_digit(n)
	elif n < 1000:
		return translate_hund_digit(n)
	elif n == 1000:
		return 'onethousand'
def main():
	l = []
	for i in range(1,1001):
		l.append(pick_number(i))
	print(sum([len(i) for i in l]))
#	for w in l:
#		print(w)
main()
