import requests       # Importar módulo para realizar solicitudes HTTP
from bs4 import BeautifulSoup      # Importar módulo para analizar documentos HTML y XML
from datetime import date      # Importar módulo para manejar fechas

# URL del sitio web para buscar ofertas
url = 'https://www.mercadolibre.com.mx/ofertas'

# Crear archivo de texto
filename = f'Ofertas-{date.today().strftime("%Y-%m-%d")}.txt'

# Buscar productos en la página web
print("Scraping Mercado Libre...")      # Imprimir mensaje en consola
r = requests.get(url)       # Realizar solicitud GET al sitio web
soup = BeautifulSoup(r.content, 'html.parser')      # Analizar el contenido HTML obtenido

# Buscar productos con más de 40% de descuento
products_text = ""      # Inicializar cadena de texto vacía para almacenar información de los productos
for product in soup.find_all('a', {'class': 'promotion-item__link-container'}):      # Recorrer todos los elementos 'a' con la clase 'promotion-item__link-container'
    try:
        discount = int(product.find('span', {'class': 'andes-money-amount__discount'}).text.strip().replace('% OFF', ''))      # Obtener el descuento del producto
        if discount >= 40:      # Si el descuento es mayor o igual al 40%
            title = product.find('p', {'class': 'promotion-item__title'}).text.strip()      # Obtener el título del producto
            link = product['href']      # Obtener el enlace del producto
            price = product.find('span', {'class': 'andes-money-amount__fraction'}).text.strip()      # Obtener el precio del producto

            # Agregar datos del producto a la cadena de texto
            products_text += f"{title}: {discount}% de descuento\n{price}\n{link}\n\n"

            # Imprimir datos del producto en consola
            print(f"{title}: {discount}% de descuento")
            print(f"Precio: {price}")
            print(f"Enlace: {link}\n")

    except Exception as e:      # Si se produce un error al obtener la información del producto
        print(f"Error: {e}")

# Guardar datos del producto en archivo de texto
with open(filename, 'w', encoding='utf-8') as file:      # Abrir archivo en modo escritura con codificación UTF-8
    file.write(products_text)      # Escribir cadena de texto en el archivo

# Verificar que el archivo se haya cerrado correctamente
if file.closed:      # Si el archivo se ha cerrado correctamente
    print(f"Se han encontrado y guardado {len(soup.find_all('a', {'class': 'promotion-item__link-container'}))} productos con un descuento del 40% o más en el archivo '{filename}'.")
else:      # Si no se ha cerrado correctamente
    print("Error al cerrar el archivo.")