import random

def main():
    # Komputer losuje liczbę
    wylosowana = random.randint(1, 100)

    print("Zgadnij liczbę od 1 do 100!")

    while True:
        try:
            guess = int(input("Podaj swoją liczbę: "))

            if guess < wylosowana:
                print("Za mała!")
            elif guess > wylosowana:
                print("Za duża!")
            else:
                print("Brawo! Zgadłeś!")
                break
        except ValueError:
            print("To nie jest poprawna liczba. Spróbuj ponownie.")

if __name__ == '__main__':
    main()
