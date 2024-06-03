def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * recursive_power(base, exponent - 1)
print(recursive_power(2, 3))
