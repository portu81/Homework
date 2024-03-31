breed = input()
name = input()
age = int(input())
owner = input()
if age % 10 == 1 and age % 10 != 11:
    age = (f'{age} год')
elif 1 < age % 10 < 5:
    age = (f'{age} года')
else:
    age = (f'{age} лет')
pets = {
    name : {
      'Вид питомца': breed,
      'Возраст питомца': age,
      'Имя владельца': owner
    }
  }
print(pets)
