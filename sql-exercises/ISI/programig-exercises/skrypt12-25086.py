def main():
    tekst = input("Podaj sentencję: ")

    zamieniony = (
        tekst.replace('o', '0')
             .replace('e', '3')
             .replace('i', '1')
             .replace('a', '4')
    )

    print("Przekształcona sentencja:")
    print(zamieniony)

if __name__ == '__main__':
    main()
