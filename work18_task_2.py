def recursive_multiply(a, b):
    # Предположим, что b всегда неотрицательное
    if b == 0:
        return 0
    return a + recursive_multiply(a, b - 1)
print(recursive_multiply(5, 3))
