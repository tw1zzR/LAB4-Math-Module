import math

k = float(input("Введіть k: "))
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
x = float(input("Введіть x: "))
e = math.e

W = ( (6 * pow(k,3) - math.sin(a) + pow(math.cos(b),2)) * math.sqrt(math.fabs(b)) + (pow(e,x) / 3 * pow(a,7)) )
print(f"Значення виразу W = {round(W, 6)}.")
