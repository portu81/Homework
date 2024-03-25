text = input()# запрашиваем строку
if text[::] == text[-1::-1]:# создаем условие
    print('yes')
else:
    print('no')
