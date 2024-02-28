x = int(input())
i = 1
y = []
while i * i <= x:
    if x % i == 0:
        y.append(i)
        if i != x // i:
            y.append(x // i)
    i += 1
y.sort()
print(y)
