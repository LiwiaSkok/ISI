import requests
from bs4 import BeautifulSoup

def get_all_links(url):
    """Zwraca listę wszystkich hiperłączy ze strony."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Błąd pobierania strony: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    links = [a["href"] for a in soup.find_all("a", href=True)]
    return links

def main():
    url = "https://www.onet.pl/"
    linki = get_all_links(url)

    print(f"Znaleziono {len(linki)} hiperłączy:\n")
    for link in linki:
        print(link)

if __name__ == '__main__':
    main()
