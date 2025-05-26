import random
import string
from collections import Counter

# Generuje losowy ciąg 100 znaków (litery i cyfry)
ciag = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
print("Wygenerowany ciąg:")
print(ciag)

licznik = Counter(ciag)

print("\nSłownik wystąpień znaków:")
print(dict(licznik))

krotki = list(licznik.items())

print("\nLista krotek (znak, liczba wystąpień):")
print(krotki)

