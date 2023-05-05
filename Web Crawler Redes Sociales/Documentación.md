# 👤📲🕷 Documentación Web Crawler - Redes Sociales 🕷📲👤

A continuación se muestra una breve documentación del web crawler de redes sociales. Este, tiene la función y objetivo de buscar y analizar perfiles de distintas redes y usuarios para recopilar información. Al ejecutar este código, se genera una carpeta llamada "Redes Sociales" y dentro de ella se guardan las fotos de perfil de los usuarios a buscar y además se genera un txt con la información principal de los mismo, tal como sus seguidores, likes, posts, etc.
#

```python
import os
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
```
- Se importan los módulos necesarios para la ejecución del script, os es un módulo de Python que se utiliza para interactuar con el sistema operativo, en este caso se utilizará para crear la carpeta "Redes sociales" si no existe. 
- Requests es un módulo que se utiliza para realizar solicitudes HTTP a las páginas web. 
- BeautifulSoup es un módulo que se utiliza para analizar el contenido HTML de las páginas web y urlretrieve es un módulo que se utiliza para descargar las imágenes de perfil y guardarlas en la carpeta "Redes sociales".

```python
urls = [
    'https://www.facebook.com/zuck',
    'https://www.facebook.com/DwayneJohnson',
    'https://www.instagram.com/billieeilish/',
    'https://www.instagram.com/jeffbezos/',
]

```
En esta sección se establece una lista de URLs de perfiles de redes sociales que se desea analizar. En este caso, se han elegido cuatro perfiles de Facebook e Instagram.

```python
if not os.path.exists('Redes sociales'):
    os.mkdir('Redes sociales')

```
En esta sección se comprueba si la carpeta "Redes sociales" existe en el sistema y, en caso contrario, se crea.

```python
for url in urls:
    try:
        response = requests.get(url)
        html_content = response.content
    except requests.exceptions.RequestException as e:
        print(e)
        continue

    soup = BeautifulSoup(html_content, 'html.parser')
    name_element = soup.find('title')
    if name_element is not None:
        name = name_element.text.strip()
    else:
        name = 'Nombre no encontrado'
    profile_image_element = soup.find('meta', property='og:image')
    if profile_image_element is not None:
        profile_image_url = profile_image_element['content']
    else:
        profile_image_url = None
    description_element = soup.find('meta', property='og:description')
    if description_element is not None:
        description = description_element['content']
    else:
        description = 'Descripción no encontrada'

```
- En esta sección se itera sobre cada URL en la lista urls y se realiza el análisis correspondiente
- Primero se realiza una solicitud HTTP a la página web y se obtiene el contenido HTML. 
- Se utiliza BeautifulSoup para analizar el contenido HTML y extraer información relevante, como el nombre del perfil, la URL de la imagen de perfil y la descripción del perfil.


```python
with open(f"Redes sociales/{name}.txt", "w", encoding="utf-8") as file:
        file.write(description)

```
En este código, la línea with open(...) crea el archivo y lo mantiene abierto mientras se ejecuta el bloque de código indentado que sigue. Una vez que se sale del bloque with, el archivo se cierra automáticamente.

# 📑📂Outputs📂📑
 ## Impresión en consola del web crawler de Redes Sociales.
 
![Imagen impresión en consola del web crawler de Redes Sociales.](/Img/outputRedes.png)
 
#
 ## Generación de carpeta en la carpeta raiz.
 
 ![Imagen generación de carpeta en la carpeta raiz..](/Img/carpRedes.png)
 
#
 ## Contenido de la carpeta Redes Sociales.
 
 ![Imagen contenido de la carpeta Redes Sociales.](/Img/archivosRedes.png)
 
---

Copyright © 2023 Yessenia Paola Carbajal Armenta. 

Este proyecto se creó como parte del curso "Programación para Internet" en el año 2023.

---
