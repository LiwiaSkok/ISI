licznik = 0

print("Liczby podzielne przez 3 i 4 w przedziale 1–100:")

for i in range(1, 101):
    if i % 3 == 0 and i % 4 == 0:
        print(i)
        licznik += 1

print(f"\nLiczba takich liczb: {licznik}")
