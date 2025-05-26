import csv

def utworz_plik_pc_csv():
    with open("pc.csv", mode="w", newline='', encoding="utf-8") as plik:
        writer = csv.writer(plik, delimiter=',')
        
        # Nagłówek
        writer.writerow(["pc_name", "ip"])
        
        # Dane: 172.30.2.1 do 172.30.2.100
        for i in range(1, 101):
            pc_name = f"P{i}"
            ip = f"172.30.2.{i}"
            writer.writerow([pc_name, ip])

    print("Plik 'pc.csv' został utworzony.")

# Wywołanie funkcji
utworz_plik_pc_csv()
