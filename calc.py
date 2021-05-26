import out


def count_eyler(a, b, y, h, func):
    y_arr = [y]
    x_arr = [a]
    x = a
    i = 1
    while x + h <= b:
        new_y = y_arr[len(y_arr) - 1]
        y_arr.append(new_y + h * func.f(x, new_y))
        out.print_result(i, x, new_y, func.f(x, new_y), func.f_real(x))
        x += h
        x_arr.append(x)
        i += 1
    return x_arr, y_arr


def count_miln(a, b, y, h, func, e):
    x_arr, y_arr = count_eyler(a, min(b, a + 3.5*h), y, h, func)
    x = x_arr[len(x_arr) - 1] + h
    f_arr = []
    for i in range(1, 4):
        f_arr.append(func.f(x_arr[i], y_arr[i]))
    i = 4
    while x <= b:
        new_y = y_arr[len(y_arr) - 4] + 4 * h * (2 * f_arr[0] - f_arr[1] + 2 * f_arr[2]) / 3
        new_f = func.f(x, new_y)
        y_check = y_arr[len(y_arr) - 2] + h * (f_arr[1] + 4 * f_arr[2] + new_f) / 3
        while abs(y_check - new_y) > e:
            new_y = y_check
            new_f = func.f(x, new_y)
            y_check = y_arr[len(y_arr) - 2] + h * (f_arr[1] + 4 * f_arr[2] + new_f) / 3
        y_arr.append(new_y)
        update_f(f_arr, new_f)
        out.print_result(i, x, new_y, new_f, func.f_real(x))
        x_arr.append(x)
        x += h
        i += 1
    return x_arr, y_arr


def update_f(f, new_f):
    f[0] = f[1]
    f[1] = f[2]
    f[2] = new_f
