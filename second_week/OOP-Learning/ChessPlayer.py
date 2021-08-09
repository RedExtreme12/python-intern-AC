class ChessPlayer:

    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def __eq__(self, other):
        if isinstance(other, int) and other == self.rating:
            return True
        elif isinstance(other, ChessPlayer) and other.rating == self.rating:
            return True
        elif not isinstance(other, (int, ChessPlayer)):
            return 'Невозможно выполнить сравнение'
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, int) and self.rating > other:
            return True
        elif isinstance(other, ChessPlayer) and self.rating > other.rating:
            return True
        elif not isinstance(other, (int, ChessPlayer)):
            return 'Невозможно выполнить сравнение'
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, int) and self.rating < other:
            return True
        elif isinstance(other, ChessPlayer) and self.rating < other.rating:
            return True
        elif not isinstance(other, (int, ChessPlayer)):
            return 'Невозможно выполнить сравнение'
        else:
            return False


if __name__ == '__main__':
    magnus = ChessPlayer('Carlsen', 'Magnus', 2847)
    ian = ChessPlayer('Ian', 'Nepomniachtchi', 2789)
    print(magnus == 4000)  # False
    print(ian == 2789)  # True
    print(magnus == ian)  # False
    print(magnus > ian)  # True
    print(magnus < ian)  # False
    print(magnus < [1, 2])  # печатает "Невозможно выполнить сравнениe"
