from math import sin, cos, exp


class Func1:
    c = 0

    def f(self, x, y):
        return sin(x) + y

    def count_c(self, x0, y):
        self.c = (y + sin(x0)/2 + cos(x0)/2) / exp(x0)

    def f_real(self, x):
        return self.c * exp(x) - sin(x)/2 - cos(x)/2


class Func2:
    c = 0

    def f(self, x, y):
        return y*x

    def count_c(self, x0, y):
        self.c = y / exp((x0**2)/2)

    def f_real(self, x):
        return self.c * exp((x**2)/2)
