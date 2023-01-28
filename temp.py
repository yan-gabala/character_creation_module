from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления'
'квадратного корня из заданного числа'


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(number):
    """Вычисляет квадратный корень."""
    sq_root = calculate_square_root(number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {sq_root}')


print(message)
calc(25.5)
