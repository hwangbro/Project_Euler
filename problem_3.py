def main():
    start = 600851475143
    factor = 3
    while (start > 1):
        if start % factor == 0:
            start /= factor
        else:
            factor += 2

    return factor
    
