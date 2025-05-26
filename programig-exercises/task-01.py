# Wczytanie znaku (lub więcej znaków)
wejscie = input("Podaj znak: ")

# Sprawdzenie, czy coś w ogóle wpisano
if len(wejscie) == 0:
    print("Nie podano żadnego znaku.")
else:
    znak = wejscie[0]  # Bierze tylko pierwszy znak

    # Sposób 1: z użyciem isdigit()
    if znak.isdigit():
        print(f"(isdigit) Znak '{znak}' jest cyfrą.")
    else:
        print(f"(isdigit) Znak '{znak}' nie jest cyfrą.")

    # Sposób 2: z użyciem isinstance() 
    if isinstance(znak, str) and znak in '0123456789':
        print(f"(isinstance) Znak '{znak}' jest cyfrą.")
    else:
        print(f"(isinstance) Znak '{znak}' nie jest cyfrą.")
