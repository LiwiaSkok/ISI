from utils.obliczenia import pierwiastek, silnia, logarytm, potega

def main():
    x1 = 256
    x2 = 4
    x3 = 256
    x4 = 2
    x5 = 8

    print(f"Pierwiastek z {x1}: {pierwiastek(x1)}")
    print(f"Silnia z {x2}: {silnia(x2)}")
    print(f"Logarytm przy podstawie 2 z {x3}: {logarytm(x3, 2)}")
    print(f"{x4} do potęgi {x5}: {potega(x4, x5)}")

if __name__ == '__main__':
    main()
