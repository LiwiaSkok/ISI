tekst = input("Podaj tekst: ")
szukany = input("Podaj ciąg do wyszukania: ")

if szukany == "":
    print("Nie można szukać pustego ciągu.")
else:
    czesci = tekst.split(szukany)
    indeksy = []
    indeks = 0

    for i in range(len(czesci) - 1):
        indeks += len(czesci[i])
        indeksy.append(indeks)
        indeks += len(szukany)

    if indeksy:
        print("Znaleziono na indeksach:", indeksy)
    else:
        print("-1 (ciąg nie został znaleziony)")
