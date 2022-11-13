# Дана функция f(x) = -5*x**2 + 10*x - 150
# 1. Определить корни
# 2. Найти интервалы, на которых функция возрастает
# 3. Найти интервалы, на которых функция убывает
# 4. Построить график
# 5. Вычислить вершину
# 6. Определить промежутки, на котором f > 0
# 7. Определить промежутки, на котором f < 0
#  pip install matplotlib

import math
from simpy import *
from simpy.plotting import plot as plt
from simpy import Symbol
from sympy import minimum, maximum, Interval

x= Symbol("x")
fx = -5*x**2 + 10*x - 150
fx


# 1. Определить корни
interv = Interval(0,5)
res_min = minimum(fx,interv)
res_max = maximum(fx,interv)
diff(fx)
x1,x2 = solve(fx)
print(x1,x2)

# 2. Найти интервалы, на которых функция возрастает
solve(diff(fx)>0)

# 3. Найти интервалы, на которых функция убывает
solve(diff(fx)<0)

# 4. Построить график
p = plt(fx, (x,-5,5))

# 5. Вычислить вершину
solve(diff(fx))

# 6. Определить промежутки, на котором f > 0
print(solve(fx>0))

# 7. Определить промежутки, на котором f < 0
print(solve(fx<0))
