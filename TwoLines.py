import numpy as np
from sympy import *
from sympy.abc import y, x


class TwoLines:
    def __init__(self, eq_str1, eq_str2, x_points, x_min, x_max):
        # converts the string into a solvable equation.
        # check if y list is empty (no equations has been entered)
        if eq_str1 != '':
            self.eq_1 = sympify(eq_str1)
        else:
            self.eq_1 = None

        if eq_str2 != '':
            self.eq_2 = sympify(eq_str2)
        else:
            self.eq_2 = None

        self.x_list = np.linspace(x_min, x_max, x_points)

    def get_intersection(self):
        # solve for both equations, resulting in intercept coordination's if an intercept is present.
        # get the intersection

        try:
            result = [i.evalf() for i in solveset(self.eq_1 - self.eq_2, x, domain=S.Reals)]
            print(result)
        except TypeError:
            return "Calculation not possible"

        if len(result) == 0:
            return 'No intersect'
        else:
            # remove the imaginairy part of the equation
            x_value = [re(i) for i in result]
            # get y value for each x
            y_value = [self.eq_1.subs(x, i) for i in x_value]
            # remove the imaginairy part of the equation
            y_value = [re(i) for i in y_value]
            # zip the x and y into a tuple
            list_intersections = [(i, j) for i, j in zip(x_value, y_value)]

            return list_intersections

    def get_y(self):
        # for x, return the y-value of the two equations, result will be listed
        # check if y list is empty (no equations has been entered)
        if self.eq_1 is not None:
            list_get_1 = [self.eq_1.subs(x, i) for i in self.x_list]
        else:
            list_get_1 = []

        if self.eq_2 is not None:
            list_get_2 = [self.eq_2.subs(x, i) for i in self.x_list]
        else:
            list_get_2 = []

        return list_get_1, list_get_2
