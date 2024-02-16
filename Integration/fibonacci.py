def generate_fibonacci(limit):
    fib_sequence = []
    a, b = 0, 1
    while a <= limit:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence
