class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    def seating_capacity(self, capacity=50): # Вызываем метод seating_capacity из родительского класса
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"

bus = Autobus("Renault Logan", 180, 12) # Создаем экземпляр класса Autobus

print(bus.seating_capacity()) # Выводим результат метода seating_capacity для объекта bus
