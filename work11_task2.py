import collections

pets = { # Начальный словарь
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "Желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша"
        },
    },
}

def get_pet(ID):
    return pets.get(ID, False)

def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        suffix = 'год'
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 >= 20):
        suffix = 'года'
    else:
        suffix = 'лет'
    return suffix

def pets_list():
    for ID, pet_info in pets.items():
        for name, details in pet_info.items():
            age_suffix = get_suffix(details["Возраст питомца"])
            print(f'ID {ID}: {details["Вид питомца"]} по кличке {name}. Возраст питомца: {details["Возраст питомца"]} {age_suffix}. Имя владельца: {details["Имя владельца"]}')

def create(name, pet_type, age, owner_name):
    last_id = collections.deque(pets, maxlen=1)[0] + 1
    pets[last_id] = {
        name: {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner_name
        },
    }

def read(ID):
    pet = get_pet(ID)
    if pet:
        for name, details in pet.items():
            age_suffix = get_suffix(details["Возраст питомца"])
            print(f'Это {details["Вид питомца"]} по кличке {name}. Возраст питомца: {details["Возраст питомца"]} {age_suffix}. Имя владельца: {details["Имя владельца"]}')
    else:
        print("Питомец с таким ID не найден.")

def update(ID, name, pet_type, age, owner_name):
    if ID in pets:
        pets[ID][name] = {
            "Вид питомца": pet_type,
            "Возраст питомца": age,
            "Имя владельца": owner_name
        }
    else:
        print("Питомец с таким ID не найден.")

def delete(ID):
    if ID in pets:
        del pets[ID]
        print(f"Питомец с ID {ID} был удален.")
    else:
        print("Питомец с таким ID не найден.")

# пользовательского цикла с командами
command = ""
while command != "stop":
    command = input("Введите команду (create, read, update, delete, list, stop): ")
    if command == 'create':
        name = input("Введите имя питомца: ")
        pet_type = input("Введите вид питомца: ")
        age = int(input("Введите возраст питомца: "))
        owner_name = input("Введите имя владельца: ")
        create(name, pet_type, age, owner_name)
    elif command == 'read':
        ID = int(input("Введите ID питомца: "))
        read(ID)
    elif command == 'update':
        ID = int(input("Введите ID питомца: "))
        name = input("Введите новое имя питомца: ")
        pet_type = input("Введите новый вид питомца: ")
        age = int(input("Введите новый возраст питомца: "))
        owner_name = input("Введите имя нового владельца: ")
        update(ID, name, pet_type, age, owner_name)
    elif command == 'delete':
        ID = int(input("Введите ID питомца для удаления: "))
        delete(ID)
    elif command == 'list':
        pets_list()
    elif command != "stop":
        print("Неизвестная команда.")
