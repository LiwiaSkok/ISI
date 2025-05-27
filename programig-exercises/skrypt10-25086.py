def main():
    numer_albumu = 25086

    alfabet = ''.join([chr(i) for i in range(97, 123)])  # od 'a' (97) do 'z' (122)

    # Zapis do 1 pliku – cały alfabet jako jeden łańcuch
    with open(f"alfabet1-{numer_albumu}.txt", "w", encoding="utf-8") as plik1:
        plik1.write(alfabet)

    # Zapis do 2 pliku – każda litera w nowej linii
    with open(f"alfabet2-{numer_albumu}.txt", "w", encoding="utf-8") as plik2:
        for litera in alfabet:
            plik2.write(litera + "\n")

    print("Zakończono zapisywanie do plików.")

if __name__ == '__main__':
    main()
