# -*- coding: utf-8 -*-
__author__ = 'Carlobo'

from bs4 import BeautifulSoup
import requests

link_chapters = []
URL = "https://lightnovelstranslations.com/re-master-magic/"

if not os.path.exists("Chapters"):
    os.makedirs("Chapters")
# Realizamos la petición a la web
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code
if status_code == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html5lib")

    # Obtenemos todos los divs donde están las entradas
    entradas = html.find_all('div', {'class': 'su-spoiler-content su-clearfix'})
    for entrada in enumerate(entradas):
        links = entrada[1].find_all('a')
        for link in enumerate(links):
            link_chapters.append(link[1].get('href'))
else:
    print "Status Code %d" % status_code

for link in enumerate(link_chapters):
    URL = link[1]
    req = requests.get(URL)
    status_code = req.status_code
    if status_code == 200:
        html = BeautifulSoup(req.text, "html5lib")
        title = html.find('h1', {'class': 'entry-title'}).getText()
        file = open("Chapters/"+title, 'w');
        chapter = html.find('div', {'class': 'entry-content'})
        ps = chapter.find_all(["p","h1", "h2", "h3", "h4", "h5", "h6"])
        for p in enumerate(ps):
            file.write(p[1].getText().encode("utf-8")+"\n")
        file.close()
    else:
        print "Status Code %d" % status_code
