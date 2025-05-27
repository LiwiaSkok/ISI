def sprawdz_czy_cyfra():
   
    wejscie = input("Podaj znak: ")

    
    if len(wejscie) == 0:
        print("Nie podano żadnego znaku.")
    else:
        znak = wejscie[0]  

        if znak.isdigit():
            print(f"(isdigit) Znak '{znak}' jest cyfrą.")
        else:
            print(f"(isdigit) Znak '{znak}' nie jest cyfrą.")

        if isinstance(znak, str) and znak in '0123456789':
            print(f"(isinstance) Znak '{znak}' jest cyfrą.")
        else:
            print(f"(isinstance) Znak '{znak}' nie jest cyfrą.")

if __name__ == '__main__':
    sprawdz_czy_cyfra()
