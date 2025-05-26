import random
import string

def main():
    numer_albumu = 25086
    slownik_25086 = {}

    # bo 21 nie jest wliczane
    for i in range(10, 21):
        losowy_ciag = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        slownik_25086[i] = losowy_ciag

    print(f"slownik_{numer_albumu}:")
    for klucz, wartosc in slownik_25086.items():
        print(f"{klucz}: {wartosc}")

if __name__ == '__main__':
    main()
