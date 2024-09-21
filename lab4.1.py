import math

x = float(input("Введiть x: "))
if x < 0:
    print("Обчислити функцію неможливо. Спробуйте ще раз!")
else:
    func = ((math.sin(x + 4) - math.cos(3 * x)) / (math.sqrt(5 * x) + math.log2(math.fabs(x + 4))))
    print(f"Відповідь: f(x) = {round(func, 6)}")