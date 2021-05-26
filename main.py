import calc
import inp
import funcs
import draw


def main():
    func_num, method_num, a, b, y, h, e = inp.start()
    if func_num == 0:
        func = funcs.Func1()
    else:
        func = funcs.Func2()
    func.count_c(a, y)
    if method_num == 0:
        x_arr, y_arr = calc.count_eyler(a, b, y, h, func)
    else:
        x_arr, y_arr = calc.count_miln(a, b, y, h, func, e)
    draw.draw(x_arr, y_arr, func)


if __name__ == '__main__':
    main()