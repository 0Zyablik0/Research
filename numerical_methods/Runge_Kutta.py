from copy import deepcopy
class RungeKutta_4():
    @staticmethod
    def solve(f, x0, y0, step_size, n):
        """

        :param f: function of righ-hand side of differential equation y' = f(x, y)
        :param step_size: step of the grid
        :param n: number of steps
        :return: generates y_(i) = y(x_0 + i*h) for i = 1, ... ,n
        """
        y = y0
        x = x0
        for i in range(n):
            yield deepcopy(y)
            k1 = step_size*f(x, y)
            k2 = step_size*f(x + step_size/2, y + k1/2)
            k3 = step_size*f(x + step_size/2, y + k2/2)
            k4 = step_size*f(x + step_size, y + k3)
            y += (k1 + 2*k2 + 2*k3 + k4)/6.0
            x += step_size
        yield deepcopy(y)
    