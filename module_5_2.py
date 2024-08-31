class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей {self.numbers_of_floors}'

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.numbers_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range(1, new_floor):
                print(i)
            print(f'Вы приехали на {new_floor} этаж')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))