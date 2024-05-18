def recursive(lst, index=0):
    if index == len(lst):
        print("Конец списка")
        return
    print(lst[index]) # Вывод элемента списка
    recursive(lst, index + 1) # Вызов функции со следующим индексом

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] # Предполагаемый список

recursive(my_list) # Запуск функции
