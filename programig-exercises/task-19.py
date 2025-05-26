def czy_palindrom(tekst):
    # Usuwamy spacje i zamieniamy na małe litery
    tekst = tekst.replace(" ", "").lower()
    return tekst == tekst[::-1]

def main():
    zdanie = input("Podaj wyraz lub zdanie: ")

    if czy_palindrom(zdanie):
        print("To jest palindrom!")
    else:
        print("To nie jest palindrom.")

if __name__ == '__main__':
    main()
