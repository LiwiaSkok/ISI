from datetime import datetime

class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg

    @property
    def wiek(self):
        return datetime.now().year - self.rok_produkcji

    def is_old(self):
        return self.wiek > 10

    def is_long_mileage(self):
        return self.przebieg > 200_000


class Car(Vehicle):
    def __init__(self, nazwa, rok_produkcji, przebieg, marka):
        super().__init__(nazwa, rok_produkcji, przebieg)
        self.marka = marka

    @property
    def opis(self):
        return f"{self.marka} {self.nazwa} ({self.rok_produkcji})"


def main():
    # Obiekt klasy Vehicle
    v1 = Vehicle("Motocykl", 2005, 180000)
    print(f"- {v1.nazwa}")
    print("Wiek:", v1.wiek)
    print("Stary?", v1.is_old())
    print("Duży przebieg?", v1.is_long_mileage())
    print()

    # Obiekt klasy Car (osobny)
    c1 = Car("Civic", 2018, 90000, "Honda")
    print(f"- {c1.opis}")
    print("Wiek:", c1.wiek)
    print("Stary?", c1.is_old())
    print("Duży przebieg?", c1.is_long_mileage())
    print()

    # Obiekt klasy Car dziedziczący po Vehicle
    c2 = Car("Focus", 2010, 250000, "Ford")
    print(f"- {c2.opis}")
    print("Wiek:", c2.wiek)
    print("Stary?", c2.is_old())
    print("Duży przebieg?", c2.is_long_mileage())


if __name__ == '__main__':
    main()
