import math

def f(x):
    if x >= -0.7:
        return -6 * x**2 + math.sin(x)
    elif -9.9 < x < -0.7:
        return math.log(abs(x)) + math.sin(x)
    elif x <= -9.9:
        return 12 + math.sin(2 * x)
x = float(input("Введіть значення x: "))
print("f(x) =", f(x))
