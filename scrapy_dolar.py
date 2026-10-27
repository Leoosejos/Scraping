import requests
from bs4 import BeautifulSoup

URL = "https://www.dolar-scraping.docker.sulbaranjc.com/"

def obtener_valor() -> str:
    #1.  DESCARGAR EL HTML QUE SIRVE LA APGINA LOCAL
    respuesta = requests.get(URL, timeout=5)
    respuesta.raise_for_status()

    #2. buscar  el elememto QUE CONTIENE EL CAMBIO DESTACADO
    sopa = BeautifulSoup(respuesta.text, "html.parser")
    elemento = sopa.find(id="usd-eur-rate")
    if elemento is None:
        raise ValueError("No se encontro el elmento con el id: usd-eur-rate ")

    #3. DEVOLVER SOLO EL TEXTO DEL VALOR SON ETIQUETRAS HTML
    return elemento.get_text(strip=True)
if __name__ == "__main__":
    try:
        print(f"1 USD = {obtener_valor()} EUR")
    except (requests.RequestException, ValueError) as error:
        print(f"No se pudo obtener el cambio: {error}")
        raise SystemExit(1)