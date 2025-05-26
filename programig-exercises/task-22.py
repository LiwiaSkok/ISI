def najdluzszy_wyraz(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        slowa = [linia.strip() for linia in plik]
        najdluzsze = max(slowa, key=len)
    return najdluzsze


def wyrazy_o_dlugosci_10(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        return [slowo.strip() for slowo in plik if len(slowo.strip()) == 10]


def main():
    plik = "C:/Users/liwia/OneDrive/Pulpit/ISI/programig-exercises/wordlist_10000.txt"

    najdluzszy = najdluzszy_wyraz(plik)
    wyrazy10 = wyrazy_o_dlugosci_10(plik)

    print(f"Najdłuższy wyraz w pliku: {najdluzszy}")
    print(f"\nWszystkie wyrazy o długości 10 (łącznie: {len(wyrazy10)}):")
    print(", ".join(wyrazy10))


if __name__ == '__main__':
    main()
