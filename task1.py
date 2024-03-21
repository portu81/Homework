n = int(input())# получаем число
res = []# создаем пустой список
for i in range(n):# создаем условие
    a = int(input())
    res.append(a)# добавляем число в список
    i += 1
res.reverse()# переворачиваем список
print(*res)
