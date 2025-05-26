import math

def main():
    print("== Sposób 1: klasyczna pętla ==")
    for i in range(1, 257):
        if i % 2 == 0:
            pierwiastek = math.sqrt(i)
            print(f"√{i} = {pierwiastek}")

    print("\n== Sposób 2: list comprehension ==")
    pierwiastki = [math.sqrt(i) for i in range(1, 257) if i % 2 == 0]

    for i, p in zip(range(2, 257, 2), pierwiastki):
        print(f"√{i} = {p}")

if __name__ == '__main__':
    main()