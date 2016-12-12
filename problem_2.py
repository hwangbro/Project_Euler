def main():
    sequence = [1, 2]
    i = 0
    while True:
        next_value = sequence[i] + sequence[i+1]
        if (next_value < 4000000):
            sequence.append(next_value)
            i += 1
        else:
            break

    answer = 0
    for i in sequence:
        if i % 2 == 0:
            answer += i

    return answer
        
        
        
