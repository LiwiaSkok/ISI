import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Home:
    def __init__(self, header_name, price, price_m2):
        self.header_name = header_name
        self.price = price
        self.price_m2 = price_m2

    def return_data(self):
        return {
            'header_name': self.header_name,
            'price': self.price,
            'price_m2': self.price_m2
        }

def pobranie_postow():
    service = Service(r'C:\Users\liwia\OneDrive\Pulpit\ISI\programig-exercises\chromedriver.exe')

    driver = webdriver.Chrome(service=service)
    driver.get('https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing')

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article[data-cy='listing-item']"))
        )
    except TimeoutException:
        print("Timeout: Nie udało się załadować wszystkich ofert na czas.")
        driver.quit()
        return

    homes = []
    posts = driver.find_elements(By.CSS_SELECTOR, "article[data-cy='listing-item']")

    for post in posts:
        try:
            tytul = post.find_element(By.CLASS_NAME, 'css-16vl3c1').text
            cena = post.find_element(By.CLASS_NAME, 'css-afwkhs').text

            try:
                cena_m2 = post.find_element(By.XPATH, ".//dt[text()='Cena za metr kwadratowy']/following-sibling::dd[1]/span").text
            except NoSuchElementException:
                cena_m2 = "Brak danych"

            homes.append(Home(tytul, cena, cena_m2))
        except NoSuchElementException as e:
            print(f"Nie znaleziono jakiegoś elementu: {e}")
            continue

    with open("home.csv", mode="w", newline="", encoding="utf-8") as plik:
        writer = csv.writer(plik)
        writer.writerow(["header_name", "price", "price_m2"])  # Nagłówki

        for i, home in enumerate(homes, start=1):
            data = home.return_data()
            print(f"oferta_{i}", data)
            writer.writerow([data['header_name'], data['price'], data['price_m2']])

    driver.quit()

if __name__ == '__main__':
    pobranie_postow()
