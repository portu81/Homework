def decimal_to_binary(n):
    if n <= 1:
        return str(n)
    else:
        return decimal_to_binary(n // 2) + str(n % 2)
print(decimal_to_binary(n = 13))
