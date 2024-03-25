a = list(map(int, input().strip().split()))# вводим числа в строчку через пробел
b = set()
for i in a:
    if i in b:
        print('YES')
    else:
        print('NO')
        b.add(i)
#print(b)
