n = int(input())
a = list(map(int, input().strip().split()))
assert len(a) == n, "Количество введённых чисел не равно n"# проверяем что количество чисел равняется n
a = set(a)
print(len(a))
