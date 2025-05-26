def sprawdz_liczbe(wejscie):
    wejscie = wejscie.strip()  # usuwa spacje

    if len(wejscie) < 2:
        return "Łańcuch musi mieć co najmniej dwa znaki."

    if all(char.isdigit() for char in wejscie):
        return f"To jest liczba: {wejscie}"
    else:
        return f"To nie jest liczbą: {wejscie}"

wejscie = input("Podaj łańcuch znaków: ")
print(sprawdz_liczbe(wejscie))
