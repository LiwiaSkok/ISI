import math
from utils.obliczenia import pierwiastek, silnia, logarytm, sinus

x1 = 256
x2 = 4
x3 = 10
x4 = math.pi / 2  # 90 stopni

print(f"Pierwiastek z {x1}: {pierwiastek(x1)}")
print(f"Silnia z {x2}: {silnia(x2)}")
print(f"Logarytm naturalny z {x3}: {logarytm(x3)}")
print(f"Sinus z {x4} radianów: {sinus(x4)}")
