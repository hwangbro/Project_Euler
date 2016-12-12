def main():
    largest = 0
    for i in range(1000):
        for j in range(1000):
            if str(i*j) == reverse(str(i*j)) and i*j > largest:
                largest = i*j

    return largest


def reverse(word) -> str:
    x = list(reversed(word))
    new_word = ''
    for i in x:
        new_word += i

    return new_word
        
