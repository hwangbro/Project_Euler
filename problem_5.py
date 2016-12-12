def main(step):
    divisors = [20, 19, 18, 17, 16, 14, 13, 11]
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in divisors):
            return num
        
            
        
