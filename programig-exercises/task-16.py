def potega(liczba):
    wynik = liczba ** 3
    print(f"{liczba} do trzeciej potęgi to: {wynik}")

def main():
    
    wejscie = input("Podaj liczbę: ")
    liczba = int(wejscie)
    potega(liczba)

if __name__ == '__main__':
    main()
