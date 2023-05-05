# Importar los módulos necesarios
import os                             # Para interactuar con el sistema operativo y crear la carpeta "Redes sociales" si no existe
import requests                       # Para realizar solicitudes HTTP a las páginas web
from bs4 import BeautifulSoup         # Para analizar el contenido HTML de las páginas web
from urllib.request import urlretrieve # Para descargar las imágenes de perfil y guardarlas en la carpeta "Redes sociales"

# Establecer una lista de URLs de perfiles de redes sociales que deseamos analizar
urls = [
    'https://www.facebook.com/zuck',
    'https://www.facebook.com/DwayneJohnson',
    'https://www.instagram.com/billieeilish/',
    'https://www.instagram.com/jeffbezos/',
]

# Crear una carpeta llamada "Redes sociales" si no existe
if not os.path.exists('Redes sociales'):
    os.mkdir('Redes sociales')

# Iterar sobre cada URL en la lista y realizar el análisis correspondiente
for url in urls:
    # Realizar una solicitud HTTP a la página web y obtener el contenido HTML
    try:
        response = requests.get(url)
        html_content = response.content
    except requests.exceptions.RequestException as e:
        print(e)
        continue

    # Analizar el contenido HTML utilizando BeautifulSoup y extraer información relevante
    soup = BeautifulSoup(html_content, 'html.parser')
    name_element = soup.find('title')  # Buscar el elemento 'title' y obtener su contenido de texto
    if name_element is not None:
        name = name_element.text.strip()  # Eliminar los espacios en blanco y otros caracteres innecesarios del texto
    else:
        name = 'Nombre no encontrado'
    profile_image_element = soup.find('meta', property='og:image')  # Buscar el elemento 'meta' con la propiedad 'og:image' y obtener su valor
    if profile_image_element is not None:
        profile_image_url = profile_image_element['content']  # Obtener el valor del atributo 'content'
    else:
        profile_image_url = None
    description_element = soup.find('meta', property='og:description')  # Buscar el elemento 'meta' con la propiedad 'og:description' y obtener su valor
    if description_element is not None:
        description = description_element['content']  # Obtener el valor del atributo 'content'
    else:
        description = 'Descripción no encontrada'

    # Guardar la descripción en un archivo de texto con el nombre de la cuenta correspondiente
    with open(f"Redes sociales/{name}.txt", "w", encoding="utf-8") as file:
        file.write(description)

    # Descargar la imagen de perfil y guardarla en la carpeta "Redes sociales" con el nombre de la cuenta correspondiente
    if profile_image_url is not None:
        urlretrieve(profile_image_url, f"Redes sociales/{name}.jpg")  # Descargar la imagen y guardarla en la carpeta "Redes sociales" con el nombre de la cuenta correspondiente
