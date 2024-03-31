breed = input() # вводим данные
name = input()
age = int(input())
owner = input()
if age % 10 == 1 and age % 10 != 11: # создаем условие для возвраста
    age = (f'{age} год')
elif 1 < age % 10 < 5:
    age = (f'{age} года')
else:
    age = (f'{age} лет')
pets = { #создаем словарь в котором значения это переменные
    name : {
      'Вид питомца': breed,
      'Возраст питомца': age,
      'Имя владельца': owner
    }
  }
print(pets) # выводим словарь
