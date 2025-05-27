def znajdz_liczby():
    tabela = []

    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            tabela.append(i)

    print("Liczby podzielne przez 3 lub 5:")
    print(tabela)

if __name__ == '__main__':
    znajdz_liczby()
