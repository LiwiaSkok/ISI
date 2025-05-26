def potega(liczba):
    wynik = liczba ** 3
    print(f"{liczba} do trzeciej potęgi to: {wynik}")

# Pobranie liczby od użytkownika
wejscie = input("Podaj liczbę: ")

# Konwersja na liczbę całkowitą
liczba = int(wejscie)

# Wywołanie funkcji
potega(liczba)
