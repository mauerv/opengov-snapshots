import requests
import csv
import os.path
from os import path

# Checks if an url is a downloadable file


def is_downloadable(url):
    h = requests.head(url, allow_redirects=True, verify=False)
    header = h.headers
    content_type = header.get('content-type')
    if 'text' in content_type.lower():
        return False
    if 'html' in content_type.lower():
        return False
    return True


# # Leer el CSV con dataset links.
f = open('distribuciones.csv')
reader = csv.reader(f)

# # Select headers and skip fist line for analysis.
headers = next(reader)

# # Poner todos los links de descarga en un solo lugar.
download_links = []
for row in reader:
    download_links.append([row[15], row[3], row[4]])

# # Crear una nueva sub-carpeta llamada "data".
if not path.exists('data'):
    os.mkdir('data')

# # Descargar todos los datasets a la carpeta hija.
for link in download_links:
    file_name = f'{link[1]}_{link[2]}'
    file_path = os.path.join('data', file_name)
    if not path.exists(file_path):
        try:
            r = requests.get(link[0], allow_redirects=True, verify=False)
            open(file_path, 'wb').write(r.content)
        except:
            print(f'Could not save url: {link[0]}')
