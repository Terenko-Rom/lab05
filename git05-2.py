def is_common_divisor(y, x1, x2, x3):
    return x1 % y == 0 and x2 % y == 0 and x3 % y == 0
x1 = int(input("Введіть число x1: "))
x2 = int(input("Введіть число x2: "))
x3 = int(input("Введіть число x3: "))
y = int(input("Введіть число y: "))
if is_common_divisor(y, x1, x2, x3):
    print(f"{y} є спільним дільником чисел {x1}, {x2}, {x3}")
else:
    print(f"{y} не є спільним дільником чисел {x1}, {x2}, {x3}")