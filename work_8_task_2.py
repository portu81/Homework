import re# импортируем модуль re, с помощью которого можно последовательно идущие символы поменять на один
text = input()# запрашиваем строку
print(re.sub(r'\s+', ' ', text))# применяем модуль re.sub