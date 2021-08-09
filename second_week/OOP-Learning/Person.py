class Person:

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = gender

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        if self.gender == 'female':
            return f'Гражданка {self.surname} {self.name}'

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value == 'female':
            self.__gender = 'female'
        elif value in ('male', ''):
            self.__gender = 'male'
        else:
            print('Не знаю, что вы имели ввиду? Пусть это будет мальчик!')
            self.__gender = 'male'


if __name__ == '__main__':
    p1 = Person('Chuck', 'Norris')
    print(p1)  # печатает "Гражданин Norris Chuck"
    p2 = Person('Mila', 'Kunis', 'female')
    print(p2)  # печатает "Гражданка Kunis Mila"
    p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
    print(p3)  # печатает "Гражданин Кеноби Оби-Ван"
    print(p3.__dict__)
