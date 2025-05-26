tekst = input("Podaj tekst, w którym chcesz szukać: ")
szukany = input("Podaj ciąg znaków do znalezienia: ")

indeks = tekst.find(szukany)

if indeks != -1:
    print(f"Ciąg znaleziony na pozycji: {indeks}")
else:
    print("-1 (ciąg nie został znaleziony)")
