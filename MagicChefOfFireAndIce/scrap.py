# -*- coding: utf-8 -*-
__author__ = 'Carlobo'

from bs4 import BeautifulSoup
import requests, os, re

link_chapters = []
link_subchapters = []
URL = "http://www.radianttranslations.com/bing-huo-mo-chu/"

if not os.path.exists("Chapters"):
    os.makedirs("Chapters")
#if not os.path.exists("Volumes"):
#    os.makedirs("Volumes")
# Realizamos la petición a la web
req = requests.get(URL)

# Comprobamos que la petición nos devuelve un Status Code = 200
status_code = req.status_code
if status_code == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, "html5lib")

    # Obtenemos todos los divs donde están las entradas
    content = html.find('div', {'class': 'entry-content content'})
    table = content.find('table')
    chapters = table.find_all('tr')
    for i,chapter in enumerate(chapters):
        links = chapter.find_all('a')
        for j,link in enumerate(links):
            link_subchapters.append(link.get('href'))
        link_chapters.append(link_subchapters)
        link_subchapters = []

else:
    print "Status Code %d" % status_code
for i,links in enumerate(link_chapters):
    file = open("Chapters/Chapter "+'{:03d}'.format(i+1), 'w');
    for j,link in enumerate(links):
        URL = link
        req = requests.get(URL)
        status_code = req.status_code
        if status_code == 200:
            html = BeautifulSoup(req.text, "html5lib")
            title = html.find('h1', {'class': 'entry-title'}).getText().encode("utf-8")
            file.write("\n"+"\n"+title+"\n"+"\n")
            chapter = html.find('div', {'class': 'entry-content content'})
            #file.write(chapter.getText().encode("utf-8")+"\n")
            #fileVolu.write(chapter.getText().encode("utf-8")+"\n")
            ps = chapter.find_all(["p","h1", "h2", "h3", "h4", "h5", "h6"])
            for p in enumerate(ps):
                file.write(p[1].getText().encode("utf-8")+"\n")
        else:
            print "Status Code %d" % status_code
    file.close()
