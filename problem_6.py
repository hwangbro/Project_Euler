def main():
    sum_of_squares = 0
    square_of_sums = 0

    total_sum = 0
    for i in range(101):
        total_sum += i

    square_of_sums = total_sum ** 2

    for i in range(101):
        sum_of_squares += i ** 2

    return square_of_sums - sum_of_squares
        
