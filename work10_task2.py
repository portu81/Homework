my_dict = {i: i**i for i in range(10, -6, -1)}# Создаем словарь, используя генератор словарей и цикл for
for key in my_dict:# Выводим результат
    print(f"{key}: {my_dict[key]}")
