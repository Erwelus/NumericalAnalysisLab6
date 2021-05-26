def read_specified_num(*cases):
    while True:
        try:
            num = int(input())
            for case in cases:
                if num == case:
                    return num
            print('Некорректный ввод, введите один из предложенных вариантов')
        except ValueError:
            print('Некорректный ввод, введите один из предложенных вариантов')


def read_pair_from_console(message):
    while True:
        try:
            num = input(message)
            x, y = num.split(' ', 2)
            return float(x), float(y)
        except ValueError:
            print(f'Некорректный ввод')


def read_num_with_bounders(message, low, high):
    while True:
        try:
            num = float(input(message))
            if low < num <= high:
                return num
            print(f'Некорректный ввод, введите целое от {low} до {high}')
        except ValueError:
            print(f'Некорректный ввод, введите целое от {low} до {high}')


def read_num_with_lower_bounder(message, low):
    while True:
        try:
            num = float(input(message))
            if num >= low:
                return num
            print(f'Некорректный ввод, введите целое число не меньше {low}')
        except ValueError:
            print(f'Некорректный ввод, введите целое число не меньше {low}')


def read_number(message):
    while True:
        try:
            x = input(message)
            return float(x)
        except ValueError:
            print(f'Некорректный ввод')


def start():
    print('Эта программа предназначена для решения дифференциальных уравнений')
    print('Выберите уравнение:')
    print("[ 0 ]: y' = sin(x) + y ")
    print("[ 1 ]: y' = y*x")
    func_num = read_specified_num(0, 1)
    print('Выберите метод:')
    print("[ 0 ]: Метод Эйлера")
    print("[ 1 ]: Метод Милна")
    method_num = read_specified_num(0, 1)
    print('Введите границы интервала:')
    a = read_number("Введите левую границу интервала: ")
    b = read_num_with_lower_bounder("Введите правую границу интервала: ", a+1)
    y = read_number("Введите y0: ")
    h = read_num_with_bounders("Введите размер шага: ", 0, (b-a)/2)
    e = read_num_with_lower_bounder("Введите точность: ", 1e-10)
    return func_num, method_num, a, b, y, h, e


def read_output_format():
    print('Выберите формат вывода данных:')
    print('[ 0 ]: Вывод в консоль')
    print('[ 1 ]: Вывод в файл')
    return read_specified_num(0, 1)
