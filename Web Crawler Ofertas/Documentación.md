# DOCUMENTACIÓN WEB CRAWLER OFERTAS

A continuación se muestra una breve documentación del web crawler de ofertas. El cual básicamente tiene la función de hacer Scraping en la página de ofertas de Mercado Libre México para buscar todos aquellos productos que tengas un 40% de descuento o más y crea un archivo txt donde guarda datos de cada producto, tales como el nombre, el porcentaje de descuento, el precio y el enlace del producto. Además, los imprime en consola.
 # 

```python
import requests
from bs4 import BeautifulSoup
from datetime import date
```
- Se importa la librería requests que se utiliza para realizar solicitudes HTTP en Python.
- Se importa la clase BeautifulSoup de la librería bs4 que se utiliza para analizar el contenido HTML.
- Se importa la clase date del módulo datetime.

```python
url = 'https://www.mercadolibre.com.mx/ofertas'

```
Se define la variable url que almacena la dirección URL del sitio web que se va a raspar.

```python
filename = f'Ofertas-{date.today().strftime("%Y-%m-%d")}.txt'

```
Se define la variable filename que almacena el nombre del archivo de texto que se va a crear para almacenar los resultados del web scraping. El nombre del archivo incluye la fecha actual en el formato 'año-mes-día'.

```python
print("Scraping Mercado Libre...")

```
Se imprime en consola un mensaje indicando que el proceso de web scraping ha comenzado.

```python
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
```
- Se realiza una solicitud HTTP GET a la URL definida en la variable url y se almacena la respuesta en la variable r.
- Se utiliza BeautifulSoup para analizar el contenido HTML de la respuesta y se almacena el resultado en la variable soup.


```python
products_text = ""
for product in soup.find_all('a', {'class': 'promotion-item__link-container'}):
    try:
        discount = int(product.find('span', {'class': 'andes-money-amount__discount'}).text.strip().replace('% OFF', ''))
        if discount >= 40:
            title = product.find('p', {'class': 'promotion-item__title'}).text.strip()
            link = product['href']
            price = product.find('span', {'class': 'andes-money-amount__fraction'}).text.strip()

            products_text += f"{title}: {discount}% de descuento\n{price}\n{link}\n\n"

            print(f"{title}: {discount}% de descuento")
            print(f"Precio: {price}")
            print(f"Enlace: {link}\n")

    except Exception as e:
        print(f"Error: {e}")
```
- Se inicializa una cadena de texto vacía llamada products_text.
- Se busca en el contenido HTML de la respuesta todas las etiquetas <a> que tengan la clase promotion-item__link-container.
- Para cada una de estas etiquetas se intenta obtener el porcentaje de descuento, el título, el enlace y el precio del producto.
- Si el porcentaje de descuento es mayor o igual a 40%, se agrega una cadena de texto que contiene el título, el porcentaje de descuento, el precio y el enlace del producto a la variable products_text.
- Se imprimen en consola los datos del producto.
- Si ocurre una excepción durante el proceso, se imprime un mensaje de error en consola.

```python
with open(filename, 'w', encoding='utf-8') as file:
    file.write(products_text)

if file.closed:
    print(f"Se han encontrado y guardado {len(soup.find_all('a', {'class': 'promotion-item__link-container'}))} productos con un descuento del 40% o más en el archivo '{filename}'.")
else
    print("Error al cerrar el archivo.")
```
- La función open() abre un archivo especificado en filename en modo de escritura ('w').
- El parámetro encoding='utf-8' especifica el formato de codificación de caracteres que se usará al escribir en el archivo.
- Se llama al método write() del objeto file para escribir la cadena products_text en el archivo.
- La cláusula with garantiza que el archivo se cerrará automáticamente al salir del bloque.
- Después de que el bloque with se completa, se verifica si el archivo se cerró correctamente utilizando el atributo closed del objeto file.
- Si file.closed es True, se imprime un mensaje que indica cuántos productos con un descuento del 40% o más se encontraron y se guardaron en el archivo especificado.
- Si file.closed es False, se imprime un mensaje de error que indica que el archivo no se cerró correctamente.
