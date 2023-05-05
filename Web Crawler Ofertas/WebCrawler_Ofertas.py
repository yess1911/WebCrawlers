import requests
from bs4 import BeautifulSoup
from datetime import date

# URL del sitio web para buscar ofertas
url = 'https://www.mercadolibre.com.mx/ofertas'

# Crear archivo de texto
filename = f'Ofertas-{date.today().strftime("%Y-%m-%d")}.txt'

# Buscar productos en la página web
print("Scraping Mercado Libre...")
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Buscar productos con más de 40% de descuento
products_text = ""
for product in soup.find_all('a', {'class': 'promotion-item__link-container'}):
    try:
        discount = int(product.find('span', {'class': 'andes-money-amount__discount'}).text.strip().replace('% OFF', ''))
        if discount >= 40:
            title = product.find('p', {'class': 'promotion-item__title'}).text.strip()
            link = product['href']
            price = product.find('span', {'class': 'andes-money-amount__fraction'}).text.strip()

            # Agregar datos del producto a la cadena de texto
            products_text += f"{title}: {discount}% de descuento\n{price}\n{link}\n\n"

            # Imprimir datos del producto en consola
            print(f"{title}: {discount}% de descuento")
            print(f"Precio: {price}")
            print(f"Enlace: {link}\n")

    except Exception as e:
        print(f"Error: {e}")

# Guardar datos del producto en archivo de texto
with open(filename, 'w', encoding='utf-8') as file:
    file.write(products_text)

# Verificar que el archivo se haya cerrado correctamente
if file.closed:
    print(f"Se han encontrado y guardado {len(soup.find_all('a', {'class': 'promotion-item__link-container'}))} productos con un descuento del 40% o más en el archivo '{filename}'.")
else:
    print("Error al cerrar el archivo.")