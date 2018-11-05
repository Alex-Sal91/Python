def generate_evens():
    numbers = []
    for num in range(1,51):
        if num % 2 == 0:
            numbers.append(num)
    return numbers


print(generate_evens())
