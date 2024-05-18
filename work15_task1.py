class Transport:
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage

   def Autobus(self):
        print(f'Название автомобиля:{self.name} Скорость:{self.max_speed} Пробег:{self.mileage}')
a = Transport("Renault Logan", 180, 12)

a.Autobus()
