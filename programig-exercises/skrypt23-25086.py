import random
import string

def main():
    # Zbiór do losowania: duże + małe litery + cyfry
    znaki = string.ascii_letters + string.digits

    # Lista na wygenerowane hasła
    hasla = []

    # Tworzenie 1000 haseł
    for _ in range(1000):
        haslo = ''.join(random.choices(znaki, k=6))
        hasla.append(haslo)

    # Zapis do pliku passwords.txt
    with open("passwords.txt", "w", encoding="utf-8") as plik:
        for h in hasla:
            plik.write(h + "\n")

    print("Wygenerowano 1000 haseł i zapisano do pliku passwords.txt.")

if __name__ == '__main__':
    main()
