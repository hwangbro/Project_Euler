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
    count = 0
    index = 0
    primes = list()
    while (index < 10001):
        if is_prime(count):
            primes.append(count)
            index += 1
            print(index)
        count += 1
    print(primes[10000])

main()
