

class Vector:

    def __init__(self, *args):
        self.values = args

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        self.__values = sorted(list(filter(lambda x: isinstance(x, int), value)))  # We leave in the list all
        # elements with the type Int and sorted that list.

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*list(map(lambda x: x + other, self.values)))
        elif isinstance(other, Vector):
            if len(self) == len(other):
                new_vector = [self.values[i] + other.values[i] for i in range(len(self))]

                return Vector(*new_vector)
            else:
                print('Сложение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector(*list(map(lambda x: x * other, self.values)))
        elif isinstance(other, Vector):
            if len(self) == len(other):
                new_vector = [self.values[i] * other.values[i] for i in range(len(self))]

                return Vector(*new_vector)
            else:
                print('Умножение векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя умножать с {other}')

    def __str__(self):
        if len(self.__values) > 0:
            return f"Вектор{tuple(sorted(self.values))}"
        else:
            return 'Пустой вектор'

    def __len__(self):
        return len(self.__values)


if __name__ == '__main__':
    v1 = Vector(1, 2, 3)
    print(v1)  # печатает "Вектор(1, 2, 3)"

    v2 = Vector(3, 4, 5)
    print(v2)  # печатает "Вектор(3, 4, 5)"
    v3 = v1 + v2
    print(v3)  # печатает "Вектор(4, 6, 8)"
    v4 = v3 + 5
    print(v4)  # печатает "Вектор(9, 11, 13)"
    v5 = v1 * 2
    print(v5)  # печатает "Вектор(2, 4, 6)"
    v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"
